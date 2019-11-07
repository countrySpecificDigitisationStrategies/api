from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractModel(models.Model):

    updated = models.DateTimeField(_('updated'), auto_now=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        abstract = True
