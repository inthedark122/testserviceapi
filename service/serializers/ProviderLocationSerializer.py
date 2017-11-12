"""
Сериализатор для локации оргиниазций с возможностью просмотра краткой информации по организации
"""

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .ProviderSerializer import ProviderShortSerializer
from ..models import ProviderLocation


class ProviderLocationSerializer(GeoFeatureModelSerializer):
    """
    Сериализатор для создания/редактирования/вывода локации организации.
    provider_id - для сохранения связи с организацией.
    provider - информация о организации.
    """

    provider_object = ProviderShortSerializer(read_only=True, source='provider')

    class Meta:
        model = ProviderLocation
        geo_field = "point"

        fields = (
            'id',
            'point_name',
            'price_for_one',
            'provider_type',
            'provider',
            'provider_object',
        )
