from .views import *
from django.urls import path, include,re_path
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
    path('api/auth/register/<int:id>', registerAPI.as_view(), name='registerAPI'),
    path('api/auth/register/', registerAPI.as_view(), name='registerAPI'),
    path('api/auth/validate/', emailandPhone.as_view(), name='emailandPhone'),
    path('flask-api/success/', success, name="success"),
    path('pydentic/', emailandPhoneusingPydentic.as_view(), name='emailandPhoneusingPydentic'),
    path('decorator/', phoneValidation.as_view(), name='validPhone'),
    path('flask-api/forbidden/', frobidden, name="forbidden"),
    path('flask-api/badrequest/', badrequest, name="badrequest"),
    re_path(r'^snapchat/(?P<ad_account_id>[0-9a-f-]+)/$',snapchat, name="snapchat"),
    re_path(r'^reddit/(?P<ad_account_id>[a-zA-Z0-9_]+)/$',reddit, name="reddit"),
    path('tiktok/', tiktok, name="tiktok"),
    path('amazon/', amazon, name="amazon"),
    path('yahoo/', yahoo, name="yahoo"),
    path('meta/<int:AD_ACCOUNT_ID>',meta, name="meta"),
    path('linkedin/<int:adAccountId>',linkedin, name="linkedin"),


    
    
]