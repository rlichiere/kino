
from django.conf.urls import url
from django.contrib.auth import views as auth_views

import forms
from .views import PeopleView

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'catalog/login.html',
                                        'authentication_form': forms.KinoAuthForm}, name='kino-login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='kino-logout'),
    url(r'^people/$', PeopleView.as_view(), name='people'),
]
