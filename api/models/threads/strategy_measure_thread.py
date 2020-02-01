from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class StrategyMeasureThread(AbstractModel):

    user = models.ForeignKey('User', related_name='strategy_measure_threads', on_delete=models.CASCADE, verbose_name=_('user'))
    strategy_measure = models.ForeignKey('StrategyMeasure', related_name='strategy_measure_threads', on_delete=models.CASCADE, verbose_name=_('strategy_measure'))

    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'))

    is_closed = models.BooleanField(_('is_closed'), default=False)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('strategy_measure_thread')
        verbose_name_plural = _('strategy_measure_threads')
