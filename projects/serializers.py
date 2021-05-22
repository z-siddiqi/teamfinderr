from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project, ProjectMembership, ProjectMembershipRequest

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "description", "members", "roles")
        model = Project


class ProjectMembershipSerializer(serializers.ModelSerializer):
    user = User(read_only=True)

    class Meta:
        fields = ("user", "message", "role")
        model = ProjectMembership


class ProjectMembershipRequestSerializer(serializers.ModelSerializer):
    to_project = ProjectSerializer(read_only=True)
    from_user = User(read_only=True)

    class Meta:
        fields = ("id", "to_project", "from_user", "status")
        model = ProjectMembershipRequest


class ProjectMembershipRequestNoStatusSerializer(ProjectMembershipRequestSerializer):
    class Meta:
        fields = ("id", "to_project", "from_user", "status")
        read_only_fields = ("status",)
        model = ProjectMembershipRequest
