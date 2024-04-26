"""Child class Checkout for the JSON Store parent class"""
# pylint: disable=import-error
from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH


# pylint: disable=too-few-public-methods
class CheckoutJsonStore(JsonStore):
    """ReservationJSON store singleton class"""

    # pylint: disable=invalid-name
    #class __CheckoutJsonStore(JsonStore):

    _file_name = JSON_FILES_PATH + "store_check_out.json"

    def __init__(self):
        super().__init__(self._file_name)

    # __instance = None
    #
    # def __new__(cls):
    #     if not CheckoutJsonStore.__instance:
    #         CheckoutJsonStore.__instance = CheckoutJsonStore.__CheckoutJsonStore()
    #     return CheckoutJsonStore.__instance
