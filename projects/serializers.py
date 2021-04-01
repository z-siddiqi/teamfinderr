from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description')
        model = Project
