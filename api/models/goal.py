from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Goal(AbstractModel):

    situation = models.ForeignKey('Situation', related_name='goals', on_delete=models.CASCADE, verbose_name=_('situation'))

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('goal')
        verbose_name_plural = _('goals')
