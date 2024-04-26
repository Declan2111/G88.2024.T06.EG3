""""Child Class stay for the JSON store class"""
import json

from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH

from uc3m_travel.hotel_management_exception import HotelManagementException


class StayJsonStore(JsonStore):
    """ReservationJSON store singleton class"""

    #class __StayJsonStore(JsonStore):
    # pylint: disable=invalid-name
    _file_name = JSON_FILES_PATH + "store_check_in.json"

    def __init__(self):
        self._data_list = []
        self._file_name = JSON_FILES_PATH + "store_check_in.json"

    def find_item(self, key, value):
        """Returns find item from parent class"""
        super().load_list_from_file()
        return super().find_item(key, value)

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

    # __instance = None
    # def __new__(_cls_):
    #     if not StayJsonStore.__instance:
    #         StayJsonStore.__instance = StayJsonStore.__StayJsonStore()
    #     return StayJsonStore.__instance


