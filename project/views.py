
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        return {}
