from django.test import TestCase
from rest_framework.test import APIClient
from .factories import ProviderFactory, ProviderLocationFactory

class ProviderLocationTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ProviderLocationTestCase, cls).setUpClass()

        cls.provider = ProviderFactory.create()

    def setUp(self):
        self.client = APIClient()

    def test_add_fail(self):
        res = self.client.post('/api/v1/provider_locations/', {})

        self.assertEqual(res.status_code, 400)

    def test_add_success(self):
        data = ProviderLocationFactory.stub().__dict__
        data['provider'] = self.provider.id
        res = self.client.post('/api/v1/provider_locations/', data)

        self.assertEqual(res.status_code, 201)

    def test_delete_success(self):
        provider_location = ProviderLocationFactory.create(provider=self.provider)
        res = self.client.delete('/api/v1/provider_locations/{}/'.format(provider_location.id))

        self.assertEqual(res.status_code, 204)

    def test_edit_success(self):
        provider_location = ProviderLocationFactory.create(provider=self.provider)
        new_data = ProviderLocationFactory.stub()
        res = self.client.patch(
            '/api/v1/provider_locations/{}/'.format(provider_location.id),
            new_data.__dict__
        )

        self.assertEqual(res.status_code, 200)
