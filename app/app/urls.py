from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', include("dashboard.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    path('admin/', admin.site.urls),
]

# Handling errors, but only if debug is set to False and there is another
# server to serve staticfiles
handler400 = 'dashboard.error_views.error_400'
handler401 = 'dashboard.error_views.error_401'
handler403 = 'dashboard.error_views.error_403'
handler404 = 'dashboard.error_views.error_404'
handler500 = 'dashboard.error_views.error_500'
handler503 = 'dashboard.error_views.error_503'
