from django.contrib import admin
from main.models import Service, Doctor, Record


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'customer']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'surname', 'name', 'patronymic',
                    'specialization', 'qualification', 'experience', 'avatar']


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'client', 'record_date', 'record_time', 'doctor']
