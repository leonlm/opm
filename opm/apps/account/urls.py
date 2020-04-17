from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.DefaultRouter()

router.register(r'info', AccountInfoViewSet, basename='account_info')
router.register(r'token', AccountTokenViewSet, basename='account_token')


urlpatterns = [
    path(r'login/', AccountLoginView.as_view(), name='login'),
    path(r'logout/', AccountLogoutView.as_view(), name='logout'),
    path(r'', include(router.urls))
]
