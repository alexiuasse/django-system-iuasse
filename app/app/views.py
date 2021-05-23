from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.urls import reverse


@require_http_methods(["GET"])
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('dashboard:dashboard'))
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        # return HttpResponseRedirect(reverse('website'))
        return HttpResponseRedirect(reverse('login'))
