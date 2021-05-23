from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


@require_http_methods(["GET"])
def dashboard(request):
    return render(request, template_name='dashboard.html', context={})
