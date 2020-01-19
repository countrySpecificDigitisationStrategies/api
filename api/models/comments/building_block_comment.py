from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class BuildingBlockComment(AbstractModel):

    user = models.ForeignKey('User', related_name='building_block_comments', on_delete=models.CASCADE, verbose_name=_('user'))
    building_block_thread = models.ForeignKey('BuildingBlockThread', related_name='building_block_comments', on_delete=models.CASCADE, verbose_name=_('building_block_thread'))
    parent = models.ForeignKey('BuildingBlockComment', related_name='building_block_comments', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('parent'))

    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name = _('building_block_comment')
        verbose_name_plural = _('building_block_comments')
