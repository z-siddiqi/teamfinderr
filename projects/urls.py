from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProjectViewSet

router = SimpleRouter()
router.register('', ProjectViewSet, basename='projects')

urlpatterns = router.urls
