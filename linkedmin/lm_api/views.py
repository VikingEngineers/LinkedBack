from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProjectSerializer, ProfileSerializer
from lm_projects.models import Project, Tag, Review
from lm_users.models import Profile
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProjectAPIList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    

class ProjectAPICreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]

    return Response(routes)
