
from django.conf.urls import url

from .views import ProjectView


urlpatterns = [
    url(r'^project/$', ProjectView.as_view(), name='project'),
]
