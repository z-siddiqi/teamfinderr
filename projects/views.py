from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Project, ProjectMembership, ProjectMembershipRequest
from .serializers import ProjectSerializer, ProjectMembershipSerializer, ProjectMembershipRequestSerializer
from rest_framework.response import Response


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ProjectMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMembershipSerializer

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs["project_pk"])
        members = ProjectMembership.objects.filter(project=project)
        return members

class ProjectMembershipRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMembershipRequestSerializer
    
    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs["project_pk"])
        requests = ProjectMembershipRequest.objects.filter(to_project=project)
        return requests
    
    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project_pk'])
        serializer.save(from_user=self.request.user.profile,to_project=project)

    def update(self, serializer, **kwargs):
        #permission required so that only project members can update the project request status
        #when status set to accepted, user id added to Project members list
        #query project member list, if token associated w/ one of users then access

        project = Project.objects.get(pk=self.kwargs["project_pk"])
        members = ProjectMembership.objects.filter(project=project)
        if members.filter(user=self.request.user.profile).exists():
            status = request.data['status']
            request = self.get_object()
            request.status = status 
            request.save()
            serializer = ProjectMembershipRequestSerializer(data=request)
            print(status)
            #return Response(serializer.data)
        #kwargs['partial'] = True
        #return super().update(request, *args, **kwargs)
            

            #membership_request.to_project.members.add(membership_request=from_user)
        #need to add new project to users projects portfolio
        