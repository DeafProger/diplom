from django.core.validators import MinValueValidator, MaxValueValidator
from time import gmtime, strftime, time
from datetime import timedelta, date, datetime
from django.db import models
from users.models import User


# Create your models here.
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


class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name='Услуга')
    description = models.TextField(default='', verbose_name='Описание',
                                   blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='Цена')
    customer = models.ForeignKey(Doctor, on_delete=models.CASCADE,
                                 verbose_name='Оказывает услугу',
                                 blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']


long_str2 = ('Введите желаемую дату записи от ' +
             f'{strftime("%d.%m.%Y", gmtime(int(time())+24*3600))}' +
             f' до {strftime("%d.%m.%Y", gmtime(int(time())+28*24*3600))}')
long_str = ('Желаемое время записи от ' +
            f'{strftime("%H:%M", gmtime(8*3600))}' +
            f' до {strftime("%H:%M", gmtime(18*3600))}')
CHOICES = [('Услуга пока не оказана.', 'Не оказано.'),
           ('Услуга оказана. Результаты диагностики высланы на Ваш e-mail',
            'Оказано.'),]


class Record(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="creator_record",
                               verbose_name='Клиент')
    record_date = models.DateField(verbose_name=long_str2,
                                   validators=[MaxValueValidator(date.today() +
                                               timedelta(days=28)),
                                               MinValueValidator(date.today() +
                                               timedelta(days=1))])
    record_time = models.TimeField(verbose_name=long_str,
                                   validators=[MinValueValidator(datetime.
                                               strptime('08:00', "%H:%M").
                                               time()),
                                               MaxValueValidator(datetime.
                                               strptime('18:00', "%H:%M").
                                               time())])
    doctor = models.ForeignKey(Service, max_length=100, verbose_name='Услуга',
                               on_delete=models.CASCADE)
    result = models.CharField(choices=CHOICES,
                              default='Услуга пока не оказана.')

    def __str__(self):
        return (f'{self.client.last_name} {self.client.first_name}' +
                f'{self.client.nick_name}, Вы записаны на услугу {self.doctor}'
                + f' на {self.record_date} в {self.record_time}')

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
