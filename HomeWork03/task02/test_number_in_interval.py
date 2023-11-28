import unittest

from number_in_interval import numberInInterval


class NumberInInterval(unittest.TestCase):
    def test_in_interval(self):
        self.assertTrue(numberInInterval(26))

    def test_is_not_interval(self):
        self.assertFalse(numberInInterval(24))

    def test_is_num_more_than_interval(self):
        self.assertFalse(numberInInterval(101))
