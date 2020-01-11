from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class BuildingBlock(AbstractModel):

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('building_block')
        verbose_name_plural = _('building_blocks')
