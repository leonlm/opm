from django.db import models
from common.models import ModelBaseCreate
from common.config import IS_USED


class CmdbEnv(ModelBaseCreate):
    name = models.CharField(unique=True, max_length=32)
    description = models.CharField(max_length=128)
    is_used = models.CharField(choices=IS_USED["choices"], default=IS_USED["default"], max_length=16)

    class Meta:
        db_table = 'cmdb_env'
        verbose_name = "环境信息表"
        verbose_name_plural = "环境信息表"

    def __unicode__(self):
        return self.name

