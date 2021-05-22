from django.db import models
from django.utils.translation import gettext as _


class Service(models.Model):
    """
        Class used to be like a hub to all other services!
        We need to put a OneToOne field for every type of service created! 

        Check for only one key per service? 
    """

    one_page_service = models.OneToOneField("service.OnePageService", on_delete=models.CASCADE, null=True, blank=True,
                                            verbose_name=_("Service"))


class OnePageService(models.Model):
    pass
