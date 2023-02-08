from django.test import Client, TestCase
from django.urls import reverse

from main.models import Vozac


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('main:index')
        self.vozac_url = reverse('main:vozaci')

        self.vozac1 = Vozac.objects.create(
            ime = 'some-vozac',
            prezime = 'TestName',
            OIB = '2648389752'
        )

    def test_project_homepage_get(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_vozac_get(self):
        client = Client()

        response = client.get(self.vozac_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/vozac_list.html')
