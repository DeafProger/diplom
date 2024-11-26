from main.views import (HomePageView, FeedbackView, ContactsView, AboutView,
                        ServiceListView, RecordListView, RecordCreateView,
                        RecordDetailView)
from main.apps import MainConfig
from django.urls import path


app_name = MainConfig.name

urlpatterns = [
    # Урлы для mainpage
    path('', HomePageView.as_view(), name='home_page'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('about/', AboutView.as_view(), name='about'),

    # Урлы для управления записями
    path('records/', RecordListView.as_view(), name='record_list'),
    path('record_create/', RecordCreateView.as_view(), name='record_form'),
    path('record/<int:pk>', RecordDetailView.as_view(), name='record_detail'),
    ]
