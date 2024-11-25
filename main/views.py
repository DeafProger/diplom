from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, UpdateView,
                                  CreateView, DetailView, DeleteView)
from django.urls import reverse_lazy
from main.models import Service, Doctor, Record  # and SiteMap
from users.models import User  # and SiteMap
from main.forms import RecordForm
from django.contrib.auth import get_user
from django.http import QueryDict


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Все услуги'
        return context


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class FeedbackView(TemplateView):
    template_name = 'feedback.html'


# =============================================================================
class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    template_name = 'record_list.html'
    success_url = '/records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Записи клиента {self.request.user}'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = (super().get_queryset(*args, **kwargs).
                    filter(client=self.request.user))
        return queryset


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'record_form.html'
    success_url = '/records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        context['title'] = ('Редактирование записи клиента ' +
                            f'{item.client.first_name} ' +
                            f'{item.client.last_name}')git add
        return context


class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'record_form.html'
    success_url = '/records'

    def get_form_kwargs(self, *args, **kwargs):
        queryset = super().get_form_kwargs(*args, **kwargs)
        if queryset.get('data') is None:
            queryset['data'] = QueryDict(f'client={self.request.user.pk}',
                                         mutable=True)
        # print(queryset)  # for debug
        return queryset


class RecordDetailView(DetailView):
    model = Record
    form_class = RecordForm
    template_name = 'record_detail.html'
    success_url = '/record_list'
