from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project, ProjectMembership, ProjectMembershipRequest
from accounts.serializers import CustomUserSerializer

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "description", "members", "roles")
        model = Project


class ProjectMembershipSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = ProjectMembership
        fields = ["user", "role"]


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
