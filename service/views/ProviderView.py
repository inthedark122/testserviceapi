from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from ..models import Provider
from ..serializers import ProviderSerializer


class ProviderView(viewsets.ModelViewSet):
    """
    CRUD для организации.
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = (
        SearchFilter,
    )
    search_fields = (
        'organization_name',
    )
