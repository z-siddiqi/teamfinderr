from rest_framework import serializers

from .models import Project, ProjectMembership, ProjectMembershipRequest

from profiles.serializers import UserProfileSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description','members','roles') 
        model = Project


class ProjectMembershipSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        fields = ('user', 'invite_reason','role')
        model = ProjectMembership
# we need to fix the serialiser to not return all of the users properties#


class ProjectMembershipRequestSerializer(serializers.ModelSerializer):
    to_project = ProjectSerializer(read_only=True)
    from_user = UserProfileSerializer(read_only=True)

    class Meta:
        fields = ('id', 'to_project', 'from_user', 'status','role')
        model = ProjectMembershipRequest

class ProjectMembershipRequestNoStatusSerializer(ProjectMembershipRequestSerializer):
    
    class Meta:
        fields = ('id','to_project','from_user','status','role')
        read_only_fields = ('status',)
        model = ProjectMembershipRequest
        