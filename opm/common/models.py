from django.db import models
from django.conf import settings


class ModelBaseCreate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, to_field="username", on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", default=None)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
