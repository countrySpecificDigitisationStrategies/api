from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class SituationThread(AbstractModel):

    user = models.ForeignKey('User', related_name='situation_threads', on_delete=models.CASCADE, verbose_name=_('user'))
    strategy = models.ForeignKey('Strategy', related_name='situation_threads', on_delete=models.PROTECT, verbose_name=_('strategy'))
    situation = models.ForeignKey('Situation', related_name='situation_threads', on_delete=models.PROTECT, verbose_name=_('situation'))

    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'))

    is_closed = models.BooleanField(_('is_closed'), default=False)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('situation_thread')
        verbose_name_plural = _('situation_threads')
