from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel
from api.utils import *


class UserManager(BaseUserManager):

    def create_superuser(self, email, password, **extra_fields):
        from api.models import User

        user = User.objects.create(
            email=email,

            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password(password)
        user.save()
        
        return user
