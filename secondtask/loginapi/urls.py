from .views import *
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
   
    path('api/auth/login/',loginAPI.as_view(),name="auth_login"),
    #giving access to the valid token with refresh api
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #taking the refreshed token and return new access with valid token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/helloworld1/', helloworld1.as_view(), name='helloworld1'),
    path('api/auth/helloworld2/', helloworld2.as_view(), name='helloworld2'),
    path('api/auth/refreshapi/', refreshTokenAPI.as_view(), name='refreshTokenAPI'),
    path('api/auth/register/', registerAPI.as_view(), name='registerAPI'),
   

    
]