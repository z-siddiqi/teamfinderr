from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Project, ProjectMembership, ProjectMembershipRequest
from accounts.serializers import CustomUserSerializer

User = get_user_model()


class ProjectMembershipSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = ProjectMembership
        fields = ["user", "role"]


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    def get_members(self, obj):
        qset = ProjectMembership.objects.filter(project=obj)
        return [ProjectMembershipSerializer(m).data for m in qset]

    class Meta:
        model = Project
        fields = ["id", "name", "description", "members"]


class ProjectMembershipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembershipRequest
        fields = ["id", "to_project", "from_user", "role", "status"]
        validators = [
            UniqueTogetherValidator(
                queryset=ProjectMembershipRequest.objects.all(),
                fields=["from_user", "to_project"],
                message="You have already requested to join this project!",
            )
        ]
