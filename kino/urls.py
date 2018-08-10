
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('people.urls')),
    url(r'', include('location.urls')),
    url(r'', include('catalog.urls')),
    url(r'', include('project.urls')),
]
