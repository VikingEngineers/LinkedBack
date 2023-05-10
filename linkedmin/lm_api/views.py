from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from lm_projects.models import Project, Tag, Review
from lm_users.models import Profile
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# read, update, delete a project
class ProjectAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerOrReadOnly, )


# get a list of all projects
class ProjectAPIList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# create a project
class ProjectAPICreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


# get tag list
class TagAPIList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# get all reviews of a project
class ReviewAPIList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.queryset.filter(project=self.kwargs['pk'])


# read, update, delete a review
class ReviewAPIDetail(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly, )


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'POST': 'api/users/token/'},
        {'POST': 'api/users/token/refresh/'},

        {'GET': 'api/projects/'},
        {'POST': 'api/projects/create/'},

        {'GET': 'api/projects/<str:pk>'},
        {'PUT': 'api/projects/<str:pk>'},
        {'DELETE': 'api/projects/<str:pk>'},

        {'GET': 'api/projects/<str:pk>/reviews/'},

        {'GET': 'api/review/<str:pk>/'},
        {'DELETE': 'api/review/<str:pk>/'},

        {'GET': 'api/tags/'},
    ]

    return Response(routes)
