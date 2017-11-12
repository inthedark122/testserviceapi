from factory import Faker
from factory.django import DjangoModelFactory
from ...models import Provider


class ProviderFactory(DjangoModelFactory):
    class Meta:
        model = Provider

    organization_name = Faker('company')
    email = Faker('email')
    phone_number = Faker('phone_number')
    address_main_office = Faker('address')
