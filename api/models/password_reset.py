from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class PasswordReset(AbstractModel):

    user = models.ForeignKey('User', related_name='password_resets', on_delete=models.CASCADE, verbose_name=_('user'))

    code = models.UUIDField(_('code'), default=uuid4, unique=True)

    def __str__(self):
        return '{} {}'.format(self.user.email, self.code)

    class Meta:
        verbose_name = _('password_reset')
        verbose_name_plural = _('password_resets')
