from rest_framework import serializers

from .models import Project, ProjectMembership, ProjectMembershipRequest

from profiles.serializers import UserProfileSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description')
        model = Project


class ProjectMembershipSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        fields = ('user', 'invite_reason')
        model = ProjectMembership


class ProjectMembershipRequestSerializer(serializers.ModelSerializer):
    to_project = ProjectSerializer(read_only=True)
    from_user = UserProfileSerializer(read_only=True)

    class Meta:
        fields = ('to_project', 'from_user')
        model = ProjectMembershipRequest
