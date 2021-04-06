from django.urls import path
from rest_framework_nested import routers
from .views import ProjectViewSet, ProjectMembershipViewSet

router = routers.SimpleRouter()
router.register('', ProjectViewSet, basename='projects')

project_membership_router = routers.NestedSimpleRouter(router, '', lookup='project')  # this is what is used to name the pk e.g project_pk
project_membership_router.register('members', ProjectMembershipViewSet, basename='project-members')

urlpatterns = router.urls + project_membership_router.urls
