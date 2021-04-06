from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Project, Membership
from .serializers import ProjectSerializer, MembershipSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MembershipViewSet(viewsets.ModelViewSet):
    serializer_class = MembershipSerializer

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs["project_pk"])
        members = Membership.objects.filter(project=project)
        return members
