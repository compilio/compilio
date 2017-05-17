from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^login', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url('^register', views.register, name='register')
]
