import json

from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH

from uc3m_travel.hotel_management_exception import HotelManagementException


class ReservationJsonStore(JsonStore):
    """ReservationJSON store singleton class"""

    # pylint: disable=invalid-name
    _file_name = JSON_FILES_PATH + "store_reservation.json"

    def __init__(self):
        self._data_list = []
        self._file_name = JSON_FILES_PATH + "store_reservation.json"

    def add_item(self, item):
        reservation_found = self.find_item(
            "_HotelReservation__localizer", item.localizer)
        if reservation_found:
            raise HotelManagementException("Reservation already exists")
        super().add_item(item)

    def load_list_from_file(self):
        return super().load_list_from_file()

    def save_list_to_file(self):
        return super().save_list_to_file()

    def find_item(self, key, value):
        return super().find_item(key, value)

    @property
    def data_list(self):
        return self._data_list
