from main.views import (HomePageView, FeedbackView, ContactsView, AboutView,
                        ServiceListView)
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
    ]
