
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        return {}
