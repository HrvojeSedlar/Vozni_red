from django.test import SimpleTestCase
from django.urls import resolve, reverse

from main.views import AutobusList, LinijaList, StanicaList, VozacList, index


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('main:index')
        self.assertEqual(resolve(url).func, index)

    def test_vozaci_url_is_resolved(self):
        url = reverse('main:vozaci')
        self.assertEqual(resolve(url).func.view_class, VozacList)

    def test_autobusi_url_is_resolved(self):
        url = reverse('main:autobusi')
        self.assertEqual(resolve(url).func.view_class, AutobusList)

    def test_stanice_url_is_resolved(self):
        url = reverse('main:stanice')
        self.assertEqual(resolve(url).func.view_class, StanicaList)

    def test_linije_url_is_resolved(self):
        url = reverse('main:linije')
        self.assertEqual(resolve(url).func.view_class, LinijaList)
