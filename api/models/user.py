from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from api.manager import UserManager
from api.models import AbstractModel
from api.utils import *


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email'), max_length=50, unique=True)
    country = models.ForeignKey('Country', related_name='users', blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))
    firstname = models.CharField(_('firstname'), max_length=50, blank=True, null=True)
    lastname = models.CharField(_('lastname'), max_length=50, blank=True, null=True)
    current_country = models.ForeignKey('Country', related_name='current_country_users', blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('current_country'))

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


class Token(AbstractModel):

    user = models.ForeignKey('User', related_name='tokens', on_delete=models.CASCADE, verbose_name=_('user'))

    code = models.UUIDField(_('code'), default=uuid4, unique=True)

    def __str__(self):
        return '{} {}'.format(self.user.email, self.code)

    class Meta:
        verbose_name = _('token')
        verbose_name_plural = _('tokens')


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        EmailConfirmation.objects.create(user=instance)


class EmailConfirmation(AbstractModel):

    user = models.ForeignKey('User', related_name='email_confirmations', on_delete=models.CASCADE, verbose_name=_('user'))

    code = models.UUIDField(_('code'), default=uuid4, unique=True)

    def __str__(self):
        return '{} {}'.format(self.user.email, self.code)

    class Meta:
        verbose_name = _('email_confirmation')
        verbose_name_plural = _('email_confirmations')


@receiver(post_save, sender=EmailConfirmation)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        pass
        # UserService().send_email_confirmation(instance)


class PasswordReset(AbstractModel):

    user = models.ForeignKey('User', related_name='password_resets', on_delete=models.CASCADE, verbose_name=_('user'))

    code = models.UUIDField(_('code'), default=uuid4, unique=True)

    def __str__(self):
        return '{} {}'.format(self.user.email, self.code)

    class Meta:
        verbose_name = _('password_reset')
        verbose_name_plural = _('password_resets')
