from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class SituationCategory(AbstractModel):

    building_block = models.ForeignKey('BuildingBlock', related_name='situation_categories', on_delete=models.CASCADE, verbose_name=_('building_block'))

    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'))

    goal_title = models.CharField(_('goal_title'), max_length=250)
    goal_description = models.TextField(_('goal_description'))

    def __str__(self):
        return '{} - {}'.format(self.title, self.goal_title)

    class Meta:
        verbose_name = _('situation_category')
        verbose_name_plural = _('situation_categories')
