import json

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
        reservation_found = self.find_item(
            item.localizer, "_HotelReservation__localizer")
        if reservation_found:
            raise HotelManagementException("Reservation already exists")
        return super().add_item(item)

    def load_list_from_file(self):
        return super().load_list_from_file()

    def save_list_to_file(self):
        return super().save_list_to_file()

    def find_item(self, key, value):
        return super().find_item(key, value)