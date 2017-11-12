from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework_gis.filters import InBBoxFilter, DistanceToPointFilter
from ..models import ProviderLocation
from ..serializers import ProviderLocationSerializer


class ProviderLocationView(viewsets.ModelViewSet):
    """
    CRUD заполнения локации для организации.
    in_bbox - query параметр для фильтрации по координатам
    - пример: `in_bbox=-90,29,-89,35`
    - format: (min Lon, min Lat, max Lon, max Lat)
    search - query параметр для поиска по:
    - названию организации.
    point - формат данных для сохранения/обновления: "POINT(lon lat)", например: "POINT(-123.0208 44.0464)"
    """

    queryset = ProviderLocation.objects.all().prefetch_related('provider')
    serializer_class = ProviderLocationSerializer

    filter_backends = (
        SearchFilter,
        InBBoxFilter,
        DistanceToPointFilter,
    )
    bbox_filter_field = 'point'
    bbox_filter_include_overlapping = True
    search_fields = (
        'provider__organization_name',
    )
