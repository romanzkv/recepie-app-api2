from django.test import TestCase
from .calc import add

class TestCalc(TestCase):

    def test_add(self):
        """ tests that add adds two numbers """
        self.assertEqual(add(10, 7), 17)