from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import Task


class LatestEntriesFeed(Feed):
    title = "Last tasks on Compilio"
    link = "/tasks"
    description = "Last added tasks on Compilio."

    def get_object(self, request, username):
        user = User.objects.get(username=username)
        return Task.objects.filter(owners__id=user.id).order_by('id')[:5]

    @staticmethod
    def items():
        return Task.objects.order_by('id')[:5]

    def item_title(self, item):
        return item.command

    def item_link(self, item):
        return reverse('task', args=[item.id])
