import unittest

from main.Ring import Ring


class RingTest(unittest.TestCase):
    first_ring = Ring()
    second_ring = Ring()

    def test_one_ring(self):
        self.assertTrue(self.first_ring is self.second_ring)

    def test_one_ring_with_id(self):
        self.assertEqual(id(self.first_ring), id(self.second_ring))
