from main.views import HomePageView, FeedbackView, ContactsView, AboutView,logout
from main.apps import MainConfig
from django.urls import path


app_name = MainConfig.name

urlpatterns = [
    # Урлы для mainpage
    path('', HomePageView.as_view(), name='home_page'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('about/', AboutView.as_view(), name='about'),
    path('logout/', logout, name='logout'),
    ]
