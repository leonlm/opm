from rest_framework.renderers import JSONRenderer
import json
from cmdb.models import *
from cmdb.serializers import *


class Utils(object):
    def get_serializer_list(self):
        return CmdbEnvSerializer
    def get_serializer_cu(self):
        return CmdbEnvSerializerCU
    def get_serializer_retrieve(self):
        return CmdbEnvSerializerRetrieve
    def get_model(self):
        return CmdbEnv
    def get_instance(self, **kwargs):
        if kwargs.get('instance', False):
            instance = kwargs['instance']
        else:
            instance = self.get_model().objects.get(**kwargs)
        return instance
    def correct_data(self, data):
        if 'id' in data: data.pop('id')
        return data
    def save_utils(self, method, request_data, **kwargs):
        if method == "destroy":
            instance = self.get_instance(**kwargs)
            instance.delete()
            retdict = {"status": 1, "data": "", "msg": "成功"}
        else:
            if method == "create":
                serializer = self.get_serializer_cu()(data=self.correct_data(request_data))
            else:
                instance = self.get_instance(**kwargs)
                serializer = self.get_serializer_cu()(instance, data=request_data, partial=True)
            if serializer.is_valid():
                instance_save = serializer.save()
                retdict = {"status": 1, 'data': serializer.data, "msg": "成功", "instance": instance_save}
            else:
                retdict = {"status": 0, "data": "", "msg": "失败，环境信息表写入失败！"+json.dumps(serializer.errors)}
        return retdict
    def filter_querysets(self, **kwargs):
        return self.get_model().objects.filter(**kwargs)
    def filter_value(self, key, **kwargs):
        return self.filter_querysets(**kwargs).values(key)[0][key]
    def filter_serializer_data(self, **kwargs):
        return self.get_serializer_list()(self.filter_querysets(**kwargs), many=True).data
    def filter_json(self, **kwargs):
        return json.loads(JSONRenderer().render(self.filter_serializer_data(**kwargs)))
    def get_serializer_data(self, **kwargs):
        return self.get_serializer_list()(self.get_instance(**kwargs)).data
    def get_json(self, **kwargs):
        return json.loads(JSONRenderer().render(self.get_serializer_data(**kwargs)))
    def filter_serializer_data_retrieve(self, **kwargs):
        return self.get_serializer_retrieve()(self.filter_querysets(**kwargs), many=True).data
    def filter_json_retrieve(self, **kwargs):
        return json.loads(JSONRenderer().render(self.filter_serializer_data_retrieve(**kwargs)))
    def get_serializer_data_retrieve(self, **kwargs):
        return self.get_serializer_retrieve()(self.get_instance(**kwargs)).data
    def get_json_retrieve(self, **kwargs):
        return json.loads(JSONRenderer().render(self.get_serializer_data_retrieve(**kwargs)))

