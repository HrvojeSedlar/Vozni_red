from django.test import TestCase

from main.models import Vozac


class Testmodels(TestCase):

    def setUp(self):
        self.vozac1 = Vozac.objects.create(
            ime = 'some-vozac',
            prezime = 'TestName',
            OIB = '2648389752'
        )

    def test_vozac(self):
        self.assertEqual(self.vozac1.ime, "some-vozac")
