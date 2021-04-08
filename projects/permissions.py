from rest_framework.permissions import IsAuthenticated, BasePermission


class IsMember(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method == "PATCH":
            project = obj.to_project
            return project.project_memberships.filter(user=request.user.profile).exists()
