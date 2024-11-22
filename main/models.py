from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name='Услуга')
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
