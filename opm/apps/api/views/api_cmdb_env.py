from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from common import viewsets
from cmdb.utils import cmdb_env


class ApiCmdbEnvViewSet(viewsets.ModelViewSetL, cmdb_env.Utils):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.get_serializer_list()

    def get_queryset(self):
        return self.get_model().objects.all()
