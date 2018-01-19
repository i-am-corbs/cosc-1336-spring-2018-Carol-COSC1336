import unittest

from src.sample.example import sum_numbers

class Test_Config(unittest.TestCase):

    def test_sum_numbers_for_1_plus_1(self):

        self.assertEqual(2, sum_numbers(1,1))

    def test_sum_numbers_for_5_plus_5(self):

        self.assertEqual(10, sum_numbers(5,5))

    def test_sum_numbers_for_25_plus_25(self):

        self.assertEqual(50, sum_numbers(25,25))
