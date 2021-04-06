from rest_framework import serializers

from .models import Project, Membership

from profiles.serializers import UserProfileSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description')
        model = Project


class MembershipSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        fields = ('user', 'invite_reason')
        model = Membership
