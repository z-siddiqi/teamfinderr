from rest_framework import serializers

from .models import CustomUser, Skill
from projects.models import Project, ProjectMembership


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "category"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description"]


class ProjectMembershipSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = ProjectMembership
        fields = ["id", "role", "category", "project"]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username"]


class CustomUserDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    memberships = ProjectMembershipSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "bio", "skills", "memberships"]
