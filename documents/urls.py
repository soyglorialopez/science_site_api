from rest_framework import routers
from .api import FileViewSet, CategoryViewSet, SuscriptionViewSet
# , LikeViewSet

router = routers.DefaultRouter()

router.register('api/files', FileViewSet, 'files')
router.register('api/category', CategoryViewSet, 'category')
router.register('api/suscription', SuscriptionViewSet, 'suscription')
# router.register('api/like', LikeViewSet, 'like')

# urlpatterns = [
    # path('forgot-password/', ForgotPasswordFormView.as_view()),
# ]
urlpatterns = router.urls 