from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class BuildingBlock(AbstractModel):

    pillar = models.ForeignKey('Pillar', related_name='building_blocks', on_delete=models.CASCADE, verbose_name=_('pillar'))

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('building_block')
        verbose_name_plural = _('building_blocks')
