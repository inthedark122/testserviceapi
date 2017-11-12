from django.core.management.base import BaseCommand

from service.tests.factories import ProviderLocationFactory, ProviderFactory


class Command(BaseCommand):
    help = 'Populate databse'


    def handle(self, *args, **options):
        for _ in range(100):
            provider = ProviderFactory.create()
            ProviderLocationFactory.create_batch(1000, provider=provider)

        print('Added 100 providers and 1000 locations for each provider')
