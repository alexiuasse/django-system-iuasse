from .models import *


def get_first_or_create(model, **kwargs):
    try:
        return model.objects.all()[:1].get()
    except model.DoesNotExist:
        _object = model().save(**kwargs)
        return _object
