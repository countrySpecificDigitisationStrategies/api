from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import AbstractModel


class Country(AbstractModel):

    name = models.CharField(_('name'), max_length=50)
    flag = models.ImageField(upload_to = 'flag/', blank=True, null=True)
    flag_circle = models.ImageField(upload_to = 'flag_circle/', blank=True, null=True)
    flag_rectangle = models.ImageField(upload_to = 'flag_rectangle/', blank=True, null=True)
    is_developing_country = models.BooleanField(_('is_developing_country'), default=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
