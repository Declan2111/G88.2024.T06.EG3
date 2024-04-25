"""Child class Checkout for the JSON Store parent class"""
from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH

from uc3m_travel.hotel_management_exception import HotelManagementException


class CheckoutJsonStore(JsonStore):
    """ReservationJSON store singleton class"""

    # pylint: disable=invalid-name
    _file_name = JSON_FILES_PATH + "store_check_out.json"

    def __init__(self):
        self._data_list = []
        self._file_name = JSON_FILES_PATH + "store_check_out.json"

    def add_item(self, item):
        self.data_list.append(item)

    # def load_list_from_file(self):
    #     """Returns load list from file from parent class"""
    #     return super().load_list_from_file()
    #
    # def save_list_to_file(self):
    #     """Returns save list to file from parent class"""
    #     return super().save_list_to_file()
    #
    def find_item(self, key, value):
        """Returns find item from parent class"""
        super().load_list_from_file()
        return super().find_item(key, value)
