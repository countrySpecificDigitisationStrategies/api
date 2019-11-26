from uuid import uuid4

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel
from api.services.user import UserService
from api.utils import *


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
