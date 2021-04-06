from django.urls import path
from rest_framework_nested import routers
from .views import ProjectViewSet, MembershipViewSet

router = routers.SimpleRouter()
router.register('', ProjectViewSet, basename='projects')

membership_router = routers.NestedSimpleRouter(router, '', lookup='project')  # this is what is used to name the pk e.g project_pk
membership_router.register('members', MembershipViewSet, basename='project-members')

urlpatterns = router.urls + membership_router.urls
