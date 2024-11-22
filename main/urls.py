from main.views import HomePageView
from main.apps import MainConfig
from django.urls import path


app_name = MainConfig.name

urlpatterns = [
    # Урлы для mainpage
    path('', HomePageView.as_view(), name='home_page'),
    ]
