from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project, ProjectMembership, ProjectMembershipRequest
from .serializers import ProjectSerializer, ProjectMembershipRequestSerializer
from .permissions import IsMember


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        user = self.request.user
        project = serializer.save()
        ProjectMembership.objects.create(role="owner", category="management", user=user, project=project)


class ProjectMembershipRequestViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembershipRequest.objects.all()
    serializer_class = ProjectMembershipRequestSerializer
    permission_classes = [IsAuthenticated, IsMember]

    def create(self, request, *args, **kwargs):
        request.data.update({"from_user": request.user.id})
        return super().create(request, *args, **kwargs)
