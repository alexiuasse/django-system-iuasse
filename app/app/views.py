from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


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


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def error_test_view(request):
    return render(request, template_name="error.html", context={'error_code': 404, 'error_text': 'Page not found!'})
