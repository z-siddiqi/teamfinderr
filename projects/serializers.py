from rest_framework import serializers

from .models import Project, ProjectMembership

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
