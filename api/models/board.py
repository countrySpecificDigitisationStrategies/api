from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Board(AbstractModel):

    country = models.OneToOneField('Country', on_delete=models.CASCADE, verbose_name=_('country'))
    users = models.ManyToManyField('User', related_name='boards', blank=True, verbose_name=_('users'))

    def __str__(self):
        return '{}'.format(self.country.name)

    class Meta:
        verbose_name = _('board')
        verbose_name_plural = _('boards')
