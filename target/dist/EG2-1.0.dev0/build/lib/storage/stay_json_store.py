""""Child Class stay for the JSON store class"""
# pylint: disable=import-error
import json
from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException


# pylint: disable=too-few-public-methods
class StayJsonStore(JsonStore):
    """ReservationJSON store singleton class"""
    _file_name = JSON_FILES_PATH + "store_check_in.json"

    # class __StayJsonStore(JsonStore):
    # pylint: disable=invalid-name

    # pylint: disable=super-init-not-called
    def __init__(self):
        super().__init__(self._file_name)

    def find_stay_checkout(self, key, value):
        """Loads the data from a file"""
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError as ex:
            raise HotelManagementException("Error: store checkin not found") from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return super().find_item(key, value)

    # __instance = None
    #
    # def __new__(cls):
    #     if not StayJsonStore.__instance:
    #         StayJsonStore.__instance = StayJsonStore.__StayJsonStore()
    #     return StayJsonStore.__instance
