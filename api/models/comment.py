from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Comment(AbstractModel):

    user = models.ForeignKey('User', related_name='comments', on_delete=models.CASCADE, verbose_name=_('user'))
    thread = models.ForeignKey('Thread', related_name='comments', on_delete=models.CASCADE, verbose_name=_('thread'))
    parent = models.ForeignKey('Comment', related_name='comments', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('parent'))

    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
