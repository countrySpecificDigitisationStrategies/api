from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class StrategyMeasureComment(AbstractModel):

    user = models.ForeignKey('User', related_name='strategy_measure_comments', on_delete=models.CASCADE, verbose_name=_('user'))
    strategy_measure_thread = models.ForeignKey('StrategyMeasureThread', related_name='strategy_measure_comments', on_delete=models.CASCADE, verbose_name=_('strategy_measure_thread'))
    parent = models.ForeignKey('StrategyMeasureComment', related_name='strategy_measure_comments', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('parent'))

    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name = _('strategy_measure_comment')
        verbose_name_plural = _('strategy_measure_comments')
