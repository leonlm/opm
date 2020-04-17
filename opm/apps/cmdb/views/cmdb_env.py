from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from common import viewsets
from rest_framework import status
from django.http.response import JsonResponse
from cmdb.utils import cmdb_env


class CmdbEnvViewSet(viewsets.ModelViewSet, cmdb_env.Utils):
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'name', 'is_used')
    search_fields = ('name',)
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.get_serializer_list()

    def get_queryset(self):
        if self.request.GET.get('page_size'):
            self.pagination_class.page_size = self.request.GET.get('page_size')
        return self.get_model().objects.all()

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.username
        retdict = self.save_utils("create", request.data)
        if 'instance' in retdict: retdict.pop('instance')
        return JsonResponse(retdict, status=status.HTTP_200_OK)
