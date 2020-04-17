from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthUsers(AbstractUser):
    displayname = models.CharField(max_length=128, default="")
    mobile = models.CharField(max_length=16, default="")

    class Meta:
        db_table = 'auth_users'
