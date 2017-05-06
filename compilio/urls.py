from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^', include('compilio.compiler.urls')),
    url(r'^admin/', admin.site.urls),
]
