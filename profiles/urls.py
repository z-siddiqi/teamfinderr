from django.urls import path
from rest_framework_nested import routers

from .views import UserProfileViewSet, UserProfileSearchView, UserProfileSkillsViewSet

router = routers.SimpleRouter()
router.register('', UserProfileViewSet, basename='profiles')

user_skills_router = routers.NestedSimpleRouter(router,'',lookup='profile')
user_skills_router.register('skills',UserProfileSkillsViewSet,basename='profile-skills')

user_projects_router = routers.NestedSimpleRouter(router, '', lookup='profile')
user_projects_router.register('projects', UserProfileProjectViewSet, basename='profile-projects')


urlpatterns = [
    path("search/", UserProfileSearchView.as_view(), name="profile-search"),
]

urlpatterns += router.urls + user_projects_router.urls + user_skills_router.urls
