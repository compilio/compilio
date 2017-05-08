from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tasks$', views.tasks, name='tasks'),
    url(r'^compiler/init$', api.init, name='init'),
]
