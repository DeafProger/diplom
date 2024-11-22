from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# from main.forms import MainForm
from main.models import Service


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        """
        mailings = Mailing.objects.all()
        clients = Client.objects.all()
        context_data['all_mailings'] = mailings.count()
        context_data['active_mailings'] = mailings.filter(status='started').count()
        context_data['active_clients'] = clients.values('email').distinct().count()
        context_data['random_blogs'] = get_blogs_from_cache().order_by('?')[:3]
        """
        return context_data
