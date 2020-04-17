from rest_framework import routers
from django.urls import path, include
from cmdb.views import *


router = routers.DefaultRouter()
router.register(r'env', CmdbEnvViewSet, basename='cmdb_env')


urlpatterns = [
    path(r'', include(router.urls)),
]
