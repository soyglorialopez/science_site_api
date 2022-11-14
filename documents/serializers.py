from rest_framework import serializers
from .models import File, Category, Suscription


class FileSerializer(serializers.ModelSerializer):

  class Meta: 
    ordering = ['-id']
    model = File
    fields = ('id', 'title', 'user_name', 'file', 'date', 'like', 'categories')
    extra_kwargs = {'categories': {'required': True}}
    read_only_fields = ['date', 'like']
class CategorySerializer(serializers.ModelSerializer):
  files = FileSerializer(many=True, read_only=True)
  class Meta: 
    ordering = ['id']
    model = Category
    fields = ('id', 'name', 'files')
    extra_kwargs = {'files': {'required': False}}

class SuscriptionSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Suscription
    fields = '__all__'