from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('compilio.compiler.urls')),
    url(r'^user/', include('compilio.user.urls')),
    url(r'^admin/', admin.site.urls),
]
