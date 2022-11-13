from .models import File, Category, Suscription
from rest_framework import viewsets, permissions, parsers
from rest_framework.decorators import action
from .serializers import FileSerializer, CategorySerializer, SuscriptionSerializer
from rest_framework.response import Response

class FileViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.AllowAny]
  serializer_class = FileSerializer
  queryset = File.objects.all()
  parser_classes = [parsers.MultiPartParser, parsers.FormParser]

  @action(detail=True, methods=['post'])
  def like(self, request, pk=None):
     file = self.get_object()
     file.like += 1
     file.save()
     return Response({'status': 200})

  @action(detail=True, methods=['delete'])
  def unlike(self, request, pk=None):
     file = self.get_object()
     file.like -= 1
     file.save()
     return Response({'status': 200})
  
class CategoryViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.AllowAny]
  serializer_class = CategorySerializer
  queryset = Category.objects.all()

class SuscriptionViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.AllowAny]
  serializer_class = SuscriptionSerializer
  queryset = Suscription.objects.all()