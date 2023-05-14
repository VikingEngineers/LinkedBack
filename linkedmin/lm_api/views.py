
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from lm_projects.models import Project, Tag, Review
from lm_users.models import Profile
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError

from .permissions import *


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# register user
class UserAPICreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerWithToken


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

# create a tag


class TagAPICreate(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


# get all reviews of a project
class ReviewAPIList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.queryset.filter(project=self.kwargs['pk'])

# create review for a specific project


class ReviewAPICreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def create(self, request, *args, **kwargs):
        owner = Profile.objects.get(username=str(request.user))
        project = Project.objects.get(id=self.kwargs['pk'])

        review = {
            "owner": owner.id,
            "project": project.id,
            "body": request.data['body'],
            "value": request.data['value']
        }
        _serializer = self.serializer_class(data=review)
        if _serializer.is_valid():
            _serializer.save()
            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)  # NOQA
        else:
            return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# read, update, delete a review
class ReviewAPIDetail(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class ProfileAPIList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileAPIDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
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
        {'GET': 'api/profiles/'},
    ]

    return Response(routes)
