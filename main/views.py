from django.shortcuts import render
from config.settings import EMAIL_HOST_USER, LOGOUT_REDIRECT_URL
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.views import auth_logout
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
# from main.forms import MainForm
from main.models import Service, Doctor


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


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        doctors = Doctor.objects.all()
        context_data['doctors'] = doctors
        return context_data


class ServiceListView(ListView):
    template_name = 'services.html'
    model = Service
    fields = ['id', 'name', 'description', 'price']
    # paginate_by = 3
    # permission_required = 'services.view_service'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Все услуги'
        return context

    # def get_template_names(self):
    #     if self.request.path == '/':
    #         return ['services/service_list.html']
    #     elif self.request.path == '/services/':
    #         return ['services/service_main.html']


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class FeedbackView(TemplateView):
    template_name = 'feedback.html'


def logout(request):
    try:
        auth_logout(request)
    finally:
        return redirect(LOGOUT_REDIRECT_URL)
