from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Project, ProjectMembership, ProjectMembershipRequest
from accounts.serializers import CustomUserSerializer

User = get_user_model()


class ProjectMembershipDetailSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = ProjectMembership
        fields = ["id", "role", "category", "user"]


class ProjectSerializer(serializers.ModelSerializer):
    memberships = ProjectMembershipDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "memberships"]


class ProjectMembershipSerializer(serializers.ModelSerializer):  
    class Meta:
        model = ProjectMembership
        fields = ["id", "role", "category", "project"]
        read_only_fields = ["project"]


class ProjectMembershipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembershipRequest
        fields = ["id", "from_user", "to_membership", "status"]
        validators = [
            UniqueTogetherValidator(
                queryset=ProjectMembershipRequest.objects.all(),
                fields=["from_user", "to_membership"],
                message="You have already sent a request for this membership!",
            )
        ]
