from main.views import HomePageView, AboutView
from main.apps import MainConfig
from django.urls import path


app_name = MainConfig.name

urlpatterns = [
    # Урлы для mainpage
    path('', HomePageView.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about'),
    ]
