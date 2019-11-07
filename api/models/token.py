from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Token(AbstractModel):

    user = models.ForeignKey('User', related_name='tokens', on_delete=models.CASCADE, verbose_name=_('user'))

    identifier = models.CharField(_('identifier'), max_length=50, unique=True)

    def __str__(self):
        return '{} {}'.format(self.user.email, self.identifier)

    class Meta:
        verbose_name = _('token')
        verbose_name_plural = _('tokens')
