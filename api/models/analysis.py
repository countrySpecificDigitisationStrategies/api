from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Analysis(AbstractModel):

    country = models.OneToOneField('Country', on_delete=models.PROTECT, verbose_name=_('country'))

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('analysis')
        verbose_name_plural = _('analyses')
