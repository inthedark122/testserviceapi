"""
Информация о геоданных для поставщика
"""
from django.db import models
from django.contrib.gis.db import models as gis_models
from .Provider import Provider


class ProviderLocation(models.Model):
    """
    Модель расположения организации.

    point - Точка расположения
    point_name - название области
    price_for_one - цену обслуживания за единицу оказываемой услуги
    provider_type - типы оказываемых услуг в данной области
    provider - первичный ключ на организацию
    """

    point = gis_models.PointField()
    point_name = models.CharField(max_length=100)
    price_for_one = models.CharField(max_length=100)
    provider_type = models.CharField(max_length=100)
    provider = models.ForeignKey(to=Provider, related_name='location')

    def __str__(self):
        return "#{} {} - {}".format(self.id, self.point_name, self.provider.organization_name)
