from django.db import models
from django.urls import reverse_lazy


class BaseModel(models.Model):
    """
        Base model that has convenient methods that other models need to use or implement.
    """

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

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
