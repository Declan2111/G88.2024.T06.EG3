"""Contains class for tests for hotel manager singleton"""
# pylint: disable=import-error
import unittest
from uc3m_travel import HotelManager


class TestSingletonHotelManagerTest(unittest.TestCase):
    """Class containing tests for hotel manager singleton"""
    def test_singleton_hotel_manager(self):
        """Singleton tests for hotel manager"""
        hm_1 = HotelManager()
        hm_2 = HotelManager()
        hm_3 = HotelManager()

        self.assertEqual(hm_1, hm_2)
        self.assertEqual(hm_2, hm_3)
        self.assertEqual(hm_3, hm_1)
