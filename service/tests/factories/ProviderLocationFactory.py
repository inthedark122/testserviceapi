from factory import Faker
from factory.django import DjangoModelFactory
from ...models import ProviderLocation


class ProviderLocationFactory(DjangoModelFactory):
    class Meta:
        model = ProviderLocation

    point = 'POINT(-123.0208 44.0464)'

    point_name = Faker('word')
    price_for_one = 1 # Faker('number')
    provider_type = Faker('word')
