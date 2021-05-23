from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project, ProjectMembership, ProjectMembershipRequest, Role
from .serializers import ProjectSerializer, ProjectMembershipRequestSerializer, ProjectMembershipRequestNoStatusSerializer
from .permissions import IsMember


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        user = self.request.user
        project = serializer.save()
        ProjectMembership.objects.create(user=user, project=project, role="owner")


class ProjectMembershipRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMembershipRequestSerializer
    permission_classes = [IsAuthenticated, IsMember]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "PATCH":
            req = ProjectMembershipRequest.objects.get(pk=self.kwargs["pk"])
            if req.responded == True:
                serializer_class = ProjectMembershipRequestNoStatusSerializer

        return serializer_class

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs["project_pk"])
        requests = ProjectMembershipRequest.objects.filter(to_project=project)
        return requests

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs["project_pk"])
        role, created = Role.objects.get_or_create(
            name=self.request.data["name"], category=self.request.data["category"]
        )
        try:
            serializer.save(
                from_user=self.request.user.profile, to_project=project, role=role
            )
        except IntegrityError as err:
            raise IntegrityError("You have already requested to join this project")

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)
