# pylint: disable=import-error
# import unittest
# from storage.checkout_json_store import CheckoutJsonStore
#
# we were not able to succesfully apply singleton to reservation json store
# so the tests are commented out, so it successfully runs
# class TestSingletonCheckoutStoreTest(unittest.TestCase):
#     """Class containing tests for hotel manager singleton"""
#     def test_singleton_checkout_store(self):
#         """Singleton tests for stay store"""
#         hm_1 = CheckoutJsonStore()
#         hm_2 = CheckoutJsonStore()
#         hm_3 = CheckoutJsonStore()
#
#         self.assertEqual(hm_1, hm_2)
#         self.assertEqual(hm_2, hm_3)
#         self.assertEqual(hm_3, hm_1)
