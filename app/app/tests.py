"""

sample tests

"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    def test_add_num(self):
        result = calc.add(5,4)

        self.assertEqual(result,9)
