from rest_framework.permissions import BasePermission


class IsMember(BasePermission):
    # not applied when creating objects
    def has_object_permission(self, request, view, obj):
        project = obj.to_membership.project
        return project.memberships.filter(user=request.user).exists()
