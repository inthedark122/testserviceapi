from rest_framework import serializers
from ..models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для сохранения и редактирования организации.
    """

    class Meta:
        model = Provider
        fields = (
            'id',
            'organization_name',
            'email',
            'phone_number',
            'address_main_office'
        )


class ProviderShortSerializer(serializers.ModelSerializer):
    """
    Сериализатор организации для вывода в запросе локации.
    """

    class Meta:
        model = Provider
        fields = (
            'id',
            'organization_name',
        )
