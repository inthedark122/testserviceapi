from factory import Faker, Sequence
from factory.django import DjangoModelFactory
from ...models import ProviderLocation


class ProviderLocationFactory(DjangoModelFactory):
    class Meta:
        model = ProviderLocation

    # point = 'POINT(-123.0208 44.0464)'
    point = Sequence(lambda n: 'POINT({0} {1})'.format(n/-100, n/100))

    point_name = Faker('word')
    price_for_one = 1 # Faker('number')
    provider_type = Faker('word')
