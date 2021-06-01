from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from app.models import TimeStampMixin


class Occupation(TimeStampMixin):
    """
        Model to set the Occupation, used to identify a client.
    """

    name = models.CharField(verbose_name=_("Name"),
                            max_length=128,
                            blank=False,
                            null=False)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:test_form')

    def get_change_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:change', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})

    @staticmethod
    def get_exclude_fields():
        """
            Fields of the current model that is marked to get excluded from visualization.
        """

        return ['id', 'history']

    def get_add_fields(self):
        """
            Custom fields to be added for visualization. Need to be a dict with {'name': content}
        """

        return {}

    def get_dict_data(self):
        """
            This method automatically gathers all the fields in the current model and returns them as a dictionary, used mainly to build a layout.
        """

        exclude = self.get_exclude_fields()
        data = dict([(field.verbose_name, getattr(self, field.name))
                    for field in self._meta.fields if field.name not in exclude])
        data.update(self.get_add_fields())
        return data


class Client(TimeStampMixin):
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
    # max_length is in real 16 (66) 9 9205-4030 but with the mask it must be 17
    phone = models.CharField(verbose_name=_("Phone"),
                             max_length=17,
                             blank=True,
                             null=True)
    birthday = models.DateField(verbose_name=_("Birthday"),
                                blank=True,
                                null=True)
    occupation = models.ForeignKey("client.Occupation",
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True,
                                   verbose_name=_("Occupation"))
    date = models.DateField(
        verbose_name=_("Date"),
        default=timezone.now,
        help_text=_("This date is used for statistics, build charts. "),
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:view')

    def get_change_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:change', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})

    @staticmethod
    def get_exclude_fields():
        """
            Fields of the current model that is marked to get excluded from visualization.
        """

        return ['id', 'history']

    def get_add_fields(self):
        """
            Custom fields to be added for visualization. Need to be a dict with {'name': content}
        """

        return {}

    def get_dict_data(self):
        """
            This method automatically gathers all the fields in the current model and returns them as a dictionary, used mainly to build a layout.
        """

        exclude = self.get_exclude_fields()
        data = dict([(field.verbose_name, getattr(self, field.name))
                    for field in self._meta.fields if field.name not in exclude])
        data.update(self.get_add_fields())
        return data
