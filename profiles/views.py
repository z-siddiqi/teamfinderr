from django.core.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework import filters, mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.middleware.csrf import get_token

from .models import UserProfile, Skill
from .serializers import UserProfileSerializer, UserProfileSkillSerializer

from projects.models import Project, ProjectMembership
from projects.serializers import ProjectSerializer

#Dedicated endpoints to acess CSRFToken in React frontend.
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        queryset = UserProfile.objects.filter(user=self.request.user)
        if queryset.exists():
            raise ValidationError("You already have a profile")
        serializer.save(user=self.request.user)


class UserProfileProjectViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = UserProfile.objects.get(pk=self.kwargs["profile_pk"])
        user_projects = Project.objects.filter(project_memberships__user=user)
        return user_projects

    def list(self, request, *args, **kwargs):
        user = UserProfile.objects.get(pk=self.kwargs["profile_pk"])
        queryset = self.get_queryset()
        progress = request.GET.get("progress", None)
        if progress:
            completed_projects = Project.completed_objects.filter(
                project_memberships__user=user
            )
            current_projects = queryset.exclude(pk__in=completed_projects)
            if progress == "completed":
                queryset = completed_projects
            else:
                queryset = current_projects
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileSearchView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username", "skills__name"]


class UserProfileSkillsViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_profile = UserProfile.objects.get(pk=self.kwargs["profile_pk"])
        skills = user_profile.skills
        return skills

    def perform_create(self, serializer):
        user = UserProfile.objects.get(pk=self.kwargs["profile_pk"])
        name = serializer.validated_data["name"]
        category = serializer.validated_data["category"]
        skill, created = Skill.objects.get_or_create(name=name, category=category)
        user.skills.add(skill)  # adds skill to user profile
