from django.contrib import admin
from main.models import Service, Doctor


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'surname', 'name', 'patronymic',
                    'specialization', 'qualification', 'experience', 'avatar']
