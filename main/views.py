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
        count = Service.objects.all().count()
        if count > 7:
            count = 7
        services = Service.objects.all().order_by('?')[:count]
        context_data['services'] = services
        return context_data
