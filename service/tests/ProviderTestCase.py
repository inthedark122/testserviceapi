from django.test import TestCase
from rest_framework.test import APIClient
# from ..models import Provider
from .factories import ProviderFactory

class ProviderTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_add_fail(self):
        res = self.client.post('/api/v1/providers/', {})

        self.assertEqual(res.status_code, 400)

    def test_add_success(self):
        res = self.client.post('/api/v1/providers/', ProviderFactory.stub().__dict__)

        self.assertEqual(res.status_code, 201)

    def test_delete_success(self):
        provider = ProviderFactory.create()
        res = self.client.delete('/api/v1/providers/{}/'.format(provider.id))

        self.assertEqual(res.status_code, 204)

    def test_edit_success(self):
        provider = ProviderFactory.create()
        new_data = ProviderFactory.stub()
        res = self.client.patch('/api/v1/providers/{}/'.format(provider.id), new_data.__dict__)

        self.assertEqual(res.status_code, 200)
