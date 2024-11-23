from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name='Услуга')
    description = models.TextField(default='', verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']
        permissions = [
            ('can_add_service', 'Может добавлять услугу'),
            ('can_change_service', 'Может изменять услугу'),
            ('can_view_service', 'Может просматривать услугу'),
        ]


class Doctor(models.Model):
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество',
                                  blank=True, null=True)
    specialization = models.TextField(max_length=511,
                                      verbose_name='Специализация')
    qualification = models.CharField(max_length=255,
                                     verbose_name='Квалификация')
    avatar = models.ImageField(upload_to='doctors/', blank=True, null=True)
    experience = models.PositiveIntegerField(verbose_name='Стаж')

    def __str__(self):
        return (f'{self.name} {self.patronymic} {self.surname}' +
                f', {self.specialization}, {self.qualification}')

    class Meta:
        verbose_name = 'врач'
        verbose_name_plural = 'врачи'
