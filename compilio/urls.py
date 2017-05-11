from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^', include('compilio.compiler.urls')),
    url(r'^user/', include('compilio.user.urls')),
    url(r'^admin/', admin.site.urls),
]
