"""Child class reservation for the JSON store class"""
# pylint: disable=import-error
from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH

from uc3m_travel.hotel_management_exception import HotelManagementException


# pylint: disable=too-few-public-methods
class ReservationJsonStore(JsonStore):
    """ReservationJSON store singleton class"""

    # pylint: disable=invalid-name
    #class __ReservationJsonStore(JsonStore):

    _file_name = JSON_FILES_PATH + "store_reservation.json"

    def __init__(self):
        super().__init__(self._file_name)

    def add_item(self, item):
        """finds a reservation based on a localizer and checks it doesn't already exist"""
        reservation_found = super().find_item(
            "_HotelReservation__localizer", item.localizer)
        if reservation_found:
            raise HotelManagementException("Reservation already exists")
        super().add_item(item)

    # __instance = None
    #
    # def __new__(cls):
    #     if not ReservationJsonStore.__instance:
    #         ReservationJsonStore.__instance = ReservationJsonStore.__ReservationJsonStore()
    #     return ReservationJsonStore.__instance
