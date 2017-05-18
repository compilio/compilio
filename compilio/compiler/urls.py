from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tasks$', views.tasks, name='tasks'),
    url(r'^tasks/(?P<task>\d+)$', views.task, name='task'),

    url(r'^compiler/init$', api.init, name='init'),
    url(r'^compiler/upload$', api.upload, name='upload'),
    url(r'^compiler/task$', api.task, name='task'),

    url(r'^doc', views.documentation, name='documentation'),
]
