from django.contrib.auth.models import AbstractUser
from django.db import models


verbose_message = 'Дата рождения в формате 31.01.1970'


class User(AbstractUser):
    username = None
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    nick_name = models.CharField(max_length=100, verbose_name='отчество',
                                 blank=True, null=True)
    birth_date = models.DateField(null=True, verbose_name=verbose_message)
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='телефон',
                             blank=True, null=True)
    token = models.CharField(max_length=100, unique=True, verbose_name='код',
                             blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} - {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
