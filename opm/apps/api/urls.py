from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.DefaultRouter()

router.register(r'env', ApiCmdbEnvViewSet, basename='api_cmdb_env')


urlpatterns = [
    path(r'', include(router.urls)),
]
