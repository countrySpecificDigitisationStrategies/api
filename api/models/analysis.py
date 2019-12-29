from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Analysis(AbstractModel):

    country = models.ForeignKey('Country', related_name='analysis', on_delete=models.PROTECT)
    content = models.TextField(_('content'), blank=True, null=True)

