"""Child class Checkout for the JSON Store parent class"""
from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH

# pylint: disable=too-few-public-methods
class CheckoutJsonStore(JsonStore):
    """ReservationJSON store singleton class"""

    #class __CheckoutJsonStore(JsonStore):

    # pylint: disable=invalid-name
    _file_name = JSON_FILES_PATH + "store_check_out.json"

    def __init__(self):
        self._data_list = []
        self._file_name = JSON_FILES_PATH + "store_check_out.json"

    def find_item(self, key, value):
        """Returns find item from parent class"""
        super().load_list_from_file()
        return super().find_item(key, value)

    # __instance = None
    # def __new__(_cls_):
    #     if not CheckoutJsonStore.__instance:
    #         CheckoutJsonStore.__instance = CheckoutJsonStore.__CheckoutJsonStore()
    #     return CheckoutJsonStore.__instance

