"""Child class reservation for the JSON store class"""
#pylint: disable=import-error
from storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH

from uc3m_travel.hotel_management_exception import HotelManagementException


class ReservationJsonStore(JsonStore):
    """ReservationJSON store singleton class"""
    _file_name = JSON_FILES_PATH + "store_reservation.json"
    #class __ReservationJsonStore(JsonStore):
    # pylint: disable=invalid-name


    def __init__(self):
        self._data_list = []
        self._file_name = JSON_FILES_PATH + "store_reservation.json"

    def add_item(self, item):
        """finds a reservation based on a localizer and checks it doesn't already exist"""
        reservation_found = self.find_item(
            "_HotelReservation__localizer", item.localizer)
        if reservation_found:
            raise HotelManagementException("Reservation already exists")
        super().add_item(item)

    def find_item(self, key, value):
        """Loads the data from the file then finds if the item exists"""
        super().load_list_from_file()
        return super().find_item(key, value)

    @property
    def data_list(self):
        """returns the data list"""
        return self._data_list

    # __instance = None
    # def __new__(_cls_):
    #     if not ReservationJsonStore.__instance:
    #         ReservationJsonStore.__instance = ReservationJsonStore.__ReservationJsonStore()
    #     return ReservationJsonStore.__instance
