from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *

urlpatterns = [

    path('', getRoutes, name='api_routes'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/projects/', ProjectAPIList.as_view(), name='projects'),
    path('api/projects/create/', ProjectAPICreate.as_view(), name='create_project'),

]
