""""Child Class stay for the JSON store class"""
import json

from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH

from uc3m_travel.hotel_management_exception import HotelManagementException


class StayJsonStore(JsonStore):
    """ReservationJSON store singleton class"""

    # pylint: disable=invalid-name
    _file_name = JSON_FILES_PATH + "store_check_in.json"

    def __init__(self):
        self._data_list = []
        self._file_name = JSON_FILES_PATH + "store_check_in.json"

    # def load_list_from_file(self):
    #     """Returns load lisr from file from parent class"""
    #     super().load_list_from_file()


    # def save_list_to_file(self):
    #     """Returns save list from file from parent class"""
    #     return super().save_list_to_file()
    #
    def find_item(self, key, value):
        """Returns find item from parent class"""
        super().load_list_from_file()
        return super().find_item(key, value)
    #
    # def add_item(self, item):
    #     """Returns add item from parent class"""
    #     super().add_item(item)

    def find_stay_checkout(self, key, value):
        """Loads the data from a file"""
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = (json.load(file))
        except FileNotFoundError as ex:
            raise HotelManagementException("Error: store checkin not found") from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return super().find_item(key, value)


