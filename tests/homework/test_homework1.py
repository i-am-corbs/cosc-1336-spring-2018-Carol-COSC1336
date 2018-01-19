import unittest

from src.homework.homework1 import get_hours_since_midnight
from src.homework.homework1 import get_minutes
from src.homework.homework1 import get_seconds

class Test_Config(unittest.TestCase):

    def test_get_hours_3800(self):
        self.assertEqual(1, get_hours_since_midnight(3800))

    def test_get_minutes_3800(self):
        self.assertEqual(3, get_minutes(3800))

    def test_get_seconds_3800(self):
        self.assertEqual(20, get_seconds(3800))

    def test_get_hours_3600(self):
        self.assertEqual(1, get_hours_since_midnight(3600))

    def test_get_minutes_3600(self):
        self.assertEqual(0, get_minutes(3600))

    def test_get_seconds_3600(self):
        self.assertEqual(0, get_seconds(3600))

    def test_get_hours_34950(self):
        self.assertEqual(9, get_hours_since_midnight(34950))

    def test_get_minutes_34950(self):
        self.assertEqual(42, get_minutes(34950))

    def test_get_seconds_34950(self):
        self.assertEqual(30, get_seconds(34950))
