from django.conf.urls import url

from . import views
from . import api
from .feeds import LatestEntriesFeed

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tasks$', views.tasks, name='tasks'),
    url(r'^task/(?P<id>[a-z0-9]+)$', views.task, name='task'),
    url(r'^task/delete/(?P<id>[a-z0-9]+)$', views.delete_task, name='delete_task'),

    url(r'^compiler/list$', api.list_compilers, name='list_compilers'),
    url(r'^compiler/init$', api.init, name='init'),
    url(r'^compiler/upload$', api.upload, name='upload'),
    url(r'^compiler/task$', api.task, name='task'),
    url(r'^compiler/get_output_files', api.get_output_files, name='get_output_files'),
    url(r'^compiler/delete_task', api.delete_task, name='delete_task'),

    url(r'^tasks/feed/(?P<username>[a-z]+)$', LatestEntriesFeed(), name='tasks_feed'),

    url(r'^doc$', views.documentation, name='documentation'),
    url(r'^terms$', views.terms, name='terms'),
]
