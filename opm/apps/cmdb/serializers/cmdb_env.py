from rest_framework import serializers
from cmdb.models import *
from common.serializers import AuthUsersSerializerR


class CmdbEnvSerializer(serializers.ModelSerializer):
    user = AuthUsersSerializerR(fields=('username', 'displayname'), read_only=True)

    class Meta:
        model = CmdbEnv
        fields = '__all__'


class CmdbEnvSerializerRetrieve(CmdbEnvSerializer):
    class Meta:
        model = CmdbEnv
        fields = '__all__'


class CmdbEnvSerializerCU(serializers.ModelSerializer):
    class Meta:
        model = CmdbEnv
        fields = '__all__'
