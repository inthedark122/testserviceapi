"""
Мысли про оптимизацию
1. Кеширование - в данном случае может привести к потери производительности,
    т.к. данные могут обновляться чаще, чем будет происходить кеширования.
    Самый простой споос это lru-cache встроенный в python.
    Сложнее - хранить кеш на уровне бд. Хранение кеша на уровне бд позволять достичь одинакового контента
    на разных микросервисах.
2. Кеширование с помощью django утилит - происходит на уровне http коннекта, что контролировать очень сложно.

Заключение:
    Кеширование применяется в зависимости от типа использования контента,
    если много данных идет на вставку, то смысла от кеширования не будет,
    можно в таком случае поднять несколько инстансов.

"""
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(ProviderLocationView, self).dispatch(*args, **kwargs)
