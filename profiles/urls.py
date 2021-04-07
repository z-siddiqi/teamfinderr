from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserProfileViewSet, UserProfileSearchView,Skill

router = SimpleRouter()
router.register('', UserProfileViewSet, basename='profile')

urlpatterns = [
    path("search/", UserProfileSearchView.as_view(), name="profile-search"),
]

urlpatterns += router.urls
