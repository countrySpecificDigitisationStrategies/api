from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Strategy(AbstractModel):

    user = models.ForeignKey('User', related_name='strategies', on_delete=models.PROTECT, verbose_name=_('user'))

    country = models.OneToOneField('Country', on_delete=models.PROTECT)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'))
    measures = models.ManyToManyField('Measure', blank=True, through='StrategyMeasureInformation', verbose_name=_('measures'))
    is_published = models.BooleanField(_('is_published'), default=False)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('strategy')
        verbose_name_plural = _('strategies')

class StrategyMeasureInformation(AbstractModel):

    strategy = models.ForeignKey('Strategy', related_name='strategy_measure_information', on_delete=models.PROTECT)
    measure = models.ForeignKey('Measure', on_delete=models.PROTECT)

    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name = _('strategy_measure')
        verbose_name_plural = _('strategy_measures')
