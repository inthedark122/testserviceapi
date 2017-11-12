"""
Информация о поставщиках
"""
from django.db import models


class Provider(models.Model):
    """
    Модель организации.

    organization_name - имя организации
    email - Електронная почта организации
    phone_number - Номер телефона организации
    address_main_office - Адрес главное офиса организации
    """

    organization_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address_main_office = models.CharField(max_length=255)

    def __str__(self):
        return "#{} {}".format(self.id, self.organization_name)
