from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Situation(AbstractModel):

    situation_category = models.ForeignKey('SituationCategory', related_name='situations', on_delete=models.CASCADE, verbose_name=_('situation_category'))

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('situation')
        verbose_name_plural = _('situations')
