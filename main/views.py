from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, UpdateView,
                                  CreateView, DetailView, DeleteView)
from main.models import Service, Doctor, Record
from main.forms import RecordForm
from django.http import QueryDict

from django.shortcuts import redirect, render
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


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

    def post(self, request, *args, **kwargs):
        if self.request:
            for e in request:
                send_mail(
                    subject='Отправлено сообщение с домашней страницы',
                    message=f'{e.decode('utf-8')}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[EMAIL_HOST_USER],
                )
            return redirect('/')
        return render(request, self.template_name)


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
    success_url = '/'

    def post(self, request, *args, **kwargs):
        if self.request:
            for e in request:
                send_mail(
                    subject='Отправлено сообщение со страницы contacts',
                    message=f'{e.decode('utf-8')}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[EMAIL_HOST_USER],
                )
            return redirect('/')
        return render(request, self.template_name)


class FeedbackView(TemplateView):
    template_name = 'feedback.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        if self.request:
            for e in request:
                send_mail(
                    subject='Отправлено сообщение со страницы feedback',
                    message=f'{e.decode('utf-8')}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[EMAIL_HOST_USER],
                )
            return redirect('/')
        return render(request, self.template_name)


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
                            f'{item.client.last_name}')
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
    success_url = '/records'


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    template_name = 'record_delete.html'
    success_url = '/records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
