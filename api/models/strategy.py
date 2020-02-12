from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Strategy(AbstractModel):

    board = models.OneToOneField('Board', on_delete=models.CASCADE, verbose_name=_('board'))

    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'))
    measures = models.ManyToManyField('Measure', through='StrategyMeasure', verbose_name=_('measures'))
    is_published = models.BooleanField(_('is_published'), default=False)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('strategy')
        verbose_name_plural = _('strategies')


class StrategyMeasure(AbstractModel):

    strategy = models.ForeignKey('Strategy', related_name='strategy_measures', on_delete=models.CASCADE)
    measure = models.ForeignKey('Measure', related_name='strategy_measures', on_delete=models.CASCADE)

    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.description or '-')

    class Meta:
        verbose_name = _('strategy_measure')
        verbose_name_plural = _('strategy_measures')
