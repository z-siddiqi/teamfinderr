from rest_framework import filters, generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import CustomUser, Skill
from .serializers import CustomUserDetailSerializer, SkillSerializer


# Create your views here.
class CustomUserAddSkillView(views.APIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data["name"]
        category = serializer.validated_data["category"]
        skill, created = Skill.objects.get_or_create(name=name, category=category)
        request.user.skills.add(skill)
        return Response(serializer.data, status=HTTP_201_CREATED)


class CustomUserRemoveSkillView(views.APIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_skill(self):
        skill_id = self.request.data.get("id")
        try:
            skill = Skill.objects.get(id=skill_id)
        except Skill.DoesNotExist:
            return None
        return skill

    def post(self, request):
        skill = self.get_skill()
        if not skill or skill not in request.user.skills.all():
            return Response(status=HTTP_400_BAD_REQUEST)
        request.user.skills.remove(skill)
        serializer = self.serializer_class(instance=skill)
        return Response(serializer.data)


class CustomUserSearchView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["username", "skills__name"]
