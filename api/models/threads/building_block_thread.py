from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class BuildingBlockThread(AbstractModel):

    user = models.ForeignKey('User', related_name='building_block_threads', on_delete=models.CASCADE, verbose_name=_('user'))
    strategy = models.ForeignKey('Strategy', related_name='building_block_threads', on_delete=models.PROTECT, verbose_name=_('strategy'))
    building_block = models.ForeignKey('BuildingBlock', related_name='building_block_threads', on_delete=models.PROTECT, verbose_name=_('building_block'))

    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('building_block_thread')
        verbose_name_plural = _('building_block_threads')
