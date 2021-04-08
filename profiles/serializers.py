from rest_framework import serializers

from .models import Skill, UserProfile


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(source="user.id", read_only=True)  # UserProfile does not have direct access to this field
    username = serializers.CharField(source="user.username", read_only=True)  # UserProfile does not have direct access to this field
    # skills = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ["user_id", "username", "bio"]
        
class UserProfileSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["name", "type"]

