from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from api.manager import UserManager
from api.models import AbstractModel, EmailConfirmation
from api.utils import *


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email'), max_length=50, unique=True)
    country = models.CharField(_('country'), max_length=50, choices=COUNTRY_CHOICES, blank=True, null=True)
    firstname = models.CharField(_('firstname'), max_length=50, blank=True, null=True)
    lastname = models.CharField(_('lastname'), max_length=50, blank=True, null=True)
    current_country = models.CharField(_('current_country'), max_length=50, choices=COUNTRY_CHOICES, blank=True, null=True)

    is_admin = models.BooleanField(_('is_admin'), default=False)
    is_representative = models.BooleanField(_('is_representative'), default=False)
    is_moderator = models.BooleanField(_('is_moderator'), default=False)

    # internal purpose
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return '{}'.format(self.email)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        EmailConfirmation.objects.create(user=instance)
