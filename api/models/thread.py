from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Thread(AbstractModel):

    user = models.ForeignKey('User', related_name='threads', on_delete=models.CASCADE, verbose_name=_('user'))
    strategy_measure = models.ForeignKey('StrategyMeasure', related_name='threads', on_delete=models.PROTECT, verbose_name=_('strategy_measure'))

    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name = _('thread')
        verbose_name_plural = _('threads')
