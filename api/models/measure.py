from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Measure(AbstractModel):

    goal = models.ForeignKey('Goal', related_name='measures', on_delete=models.CASCADE, verbose_name=_('goal'))

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('measure')
        verbose_name_plural = _('measures')
