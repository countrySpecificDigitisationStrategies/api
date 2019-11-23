from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Pillar(AbstractModel):

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True, null=True)
    image = models.ImageField(upload_to = 'pillars/', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('pillar')
        verbose_name_plural = _('pillars')
