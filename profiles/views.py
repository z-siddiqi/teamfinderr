from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework import filters, mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import UserProfile, Skill
from .serializers import UserProfileSerializer, SkillSerializer

from django.core.exceptions import ValidationError

User = get_user_model()


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    post: create user profile
    get: return user profile
    put/patch: update user profile bio
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        queryset = UserProfile.objects.filter(user=self.request.user)
        if queryset.exists():
            raise ValidationError('You already have a profile')
        serializer.save(user=self.request.user)

    
class UserProfileSearchView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username"]