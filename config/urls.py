from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts.views import CustomUserAddSkillView, CustomUserRemoveSkillView, CustomUserSearchView
from projects.views import ProjectViewSet, ProjectMembershipViewSet, ProjectMembershipRequestViewSet

schema_view = get_schema_view(
    openapi.Info(title="teamfinderr", default_version="v1"),
    public=True,
)

router = DefaultRouter()
router.register(r"requests", ProjectMembershipRequestViewSet)
router.register(r"projects", ProjectViewSet)

projects_router = NestedDefaultRouter(router, r"projects", lookup="project")
projects_router.register(r"memberships", ProjectMembershipViewSet, basename="project-memberships")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/user/add-skill/", CustomUserAddSkillView.as_view(), name="user-add-skill"),
    path("api/v1/auth/user/remove-skill/", CustomUserRemoveSkillView.as_view(), name="user-remove-skill"),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(projects_router.urls)),
    path("api/v1/search/", CustomUserSearchView.as_view(), name="user-search"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema"),
]
