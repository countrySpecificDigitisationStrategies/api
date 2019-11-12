from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Comment(AbstractModel):

    measure = models.ForeignKey('Measure', related_name='comments', on_delete=models.CASCADE, verbose_name=_('measure'))

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
