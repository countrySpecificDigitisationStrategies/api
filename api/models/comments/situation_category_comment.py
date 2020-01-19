from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class SituationCategoryComment(AbstractModel):

    user = models.ForeignKey('User', related_name='situation_category_comments', on_delete=models.CASCADE, verbose_name=_('user'))
    situation_category_thread = models.ForeignKey('SituationCategoryThread', related_name='situation_category_comments', on_delete=models.CASCADE, verbose_name=_('situation_category_thread'))
    parent = models.ForeignKey('SituationCategoryComment', related_name='situation_category_comments', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('parent'))

    description = models.TextField(_('description'))

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name = _('situation_category_comment')
        verbose_name_plural = _('situation_category_comments')
