from django.conf.urls import url

from . import views

urlpatterns = [
    url('^register', views.register, name='register')
]
