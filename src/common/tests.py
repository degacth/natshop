from django.test import TestCase
from . import utils


class UtilsTest(TestCase):
    def test_remove_list(self):
        a = ['hello', 'world']
        b = ['hello']
        result = utils.remove_list(a, b)
        self.assertEqual(result, ['world'], 'ERROR remove_list ' + str(result))
