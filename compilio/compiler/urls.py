from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tasks$', views.tasks, name='tasks'),
    url(r'^task/(?P<id>[A-Z0-9-]+)$', views.task, name='task'),

    url(r'^compiler/list$', api.list_compilers, name='list_compilers'),
    url(r'^compiler/init$', api.init, name='init'),
    url(r'^compiler/upload$', api.upload, name='upload'),
    url(r'^compiler/task$', api.task, name='task'),
    url(r'^compiler/get_output_files', api.get_output_files, name='get_output_files'),

    url(r'^doc$', views.documentation, name='documentation'),
    url(r'^terms$', views.terms, name='terms'),
]
