from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *

urlpatterns = [

    path('', getRoutes, name='api_routes'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', UserAPICreate.as_view(), name='register'),

    path('api/projects/', ProjectAPIList.as_view(), name='projects'),
    path('api/projects/create/', ProjectAPICreate.as_view(), name='create_project'),
    path('api/projects/<str:pk>/', ProjectAPIDetail.as_view(), name='project'),
    path('api/projects/<str:pk>/like/',
         LikeProject.as_view(), name='like_project'),

    path('api/projects/<str:pk>/reviews/',
         ReviewAPIList.as_view(), name='project_reviews'),
    path('api/projects/<str:pk>/reviews/create/',
         ReviewAPICreate.as_view(), name='create_review'),

    path('api/review/<str:pk>/', ReviewAPIDetail.as_view(), name='review'),

    path('api/tags/', TagAPIList.as_view(), name='tags'),
    path('api/tags/create/', TagAPICreate.as_view(), name='create_tag'),

    path('api/profiles/', ProfileAPIList.as_view(), name='profiles'),
    path('api/profile/<str:pk>/', ProfileAPIDetail.as_view(), name='profile'),

    path('api/messages/', MessageAPIList.as_view(), name='messages'),
    path('api/messages/create/', MessageAPICreate.as_view(), name='create_message'),
    path('api/messages/<str:pk>/', MessageAPIDetail.as_view(), name='message'),

    path('api/profile/<str:pk>/skills/', SkillAPIList.as_view(), name='skills'),
    path('api/skills/create/', SkillAPICreate.as_view(), name='create_skill'),
    path('api/skills/<str:pk>/', SkillAPIDetail.as_view(), name='skill'),

    path('api/search/projects/', SearchProjectsAPIList.as_view(),
         name='search_projects'),
    path('api/search/profiles/', SearchProfilesAPIList.as_view(),
         name='search_profiles'),


]
