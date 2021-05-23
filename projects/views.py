from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project, ProjectMembership, ProjectMembershipRequest
from .serializers import ProjectDetailSerializer, ProjectMembershipDetailSerializer, ProjectMembershipRequestSerializer
from .permissions import IsMember


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = "id"  # make the nested router parent lookup regex project_id
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        project = serializer.save()
        ProjectMembership.objects.create(role="owner", category="management", user=user, project=project)


class ProjectMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMembershipDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_project(self):
        project = get_object_or_404(Project, pk=self.kwargs["project_id"])
        return project

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ProjectMembership.objects.none()
        project = self.get_project()
        return ProjectMembership.objects.filter(project=project)

    def perform_create(self, serializer):
        project = self.get_project()
        serializer.save(project=project)


class ProjectMembershipRequestViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembershipRequest.objects.all()
    serializer_class = ProjectMembershipRequestSerializer
    permission_classes = [IsAuthenticated, IsMember]

    def create(self, request, *args, **kwargs):
        request.data.update({"from_user": request.user.id})
        return super().create(request, *args, **kwargs)
