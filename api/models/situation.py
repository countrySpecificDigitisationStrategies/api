from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Situation(AbstractModel):

    building_block = models.ForeignKey('BuildingBlock', related_name='situations', on_delete=models.CASCADE, verbose_name=_('building_block'))

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('situation')
        verbose_name_plural = _('situations')