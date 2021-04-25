import unittest
from src.utils.utils import *


class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_all_equal(self):
        self.assertTrue(all_equal(['X', 'X', 'X']))

    def test_all_equal_false(self):
        self.assertFalse(all_equal(['X', 'X', 'O']))
