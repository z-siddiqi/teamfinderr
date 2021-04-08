from django.core.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework import filters, mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .serializers import UserProfileSerializer

from projects.models import Project, ProjectMembership
from projects.serializers import ProjectSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        queryset = UserProfile.objects.filter(user=self.request.user)
        if queryset.exists():
            raise ValidationError('You already have a profile')
        serializer.save(user=self.request.user)


class UserProfileProjectViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_project_memberships = ProjectMembership.objects.filter(user=self.request.user.profile)
        user_projects = 1  # need to somehow get users projects
        return user_projects

    def list(self, request, *args, **kwargs):
        status = request.GET['status']
        completed_projects = Project.completed_objects.all()  # still need to filter for request.user
        current_projects = self.get_queryset().exclude(pk__in=completed_projects)
        if status == 'completed':
            self.queryset = completed_projects
        else:
            self.queryset = current_projects
        return super().list(request, *args, **kwargs)


class UserProfileSearchView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username"]
