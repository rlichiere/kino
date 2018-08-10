
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Location


class LocationView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        l = Location.objects.all()
        return {}
