from django.contrib import admin
from main.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price']

