from django.conf.urls import url, include

urlpatterns = [
    url('^/user', include('django.contrib.auth.urls')),
]
