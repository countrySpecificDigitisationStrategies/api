from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Measure(AbstractModel):

    situation = models.ForeignKey('Situation', related_name='measures', on_delete=models.CASCADE, verbose_name=_('situation'))

    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('measure')
        verbose_name_plural = _('measures')
