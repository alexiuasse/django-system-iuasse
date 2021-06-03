from .models import *


def get_first_or_create(model, **kwargs):
    """Get the first object or create a new one and return it."""
    try:
        return model.objects.all()[:1].get()
    except model.DoesNotExist:
        _object = model().save(**kwargs)
        return _object
