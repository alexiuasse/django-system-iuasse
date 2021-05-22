from django.db import models
from django.utils.translation import gettext as _
from base.models import BaseModel


class Client(BaseModel):
    """
        Model to specify a client.
    """

    name = models.CharField(verbose_name=_("Name"),
                            max_length=128)
    email = models.EmailField(verbose_name=_("E-mail"),
                              blank=True,
                              null=True)
    address = models.TextField(verbose_name=_("Address"),
                               blank=True,
                               null=True)
    phone = models.CharField(verbose_name=_("Phone"),
                             max_length=16,
                             blank=True,
                             null=True)
    birthday = models.DateField(verbose_name=_("Birthday"),
                                blank=True,
                                null=True)
    occupation = models.ForeignKey("config.Occupation",
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True,
                                   verbose_name=_("Occupation"))
