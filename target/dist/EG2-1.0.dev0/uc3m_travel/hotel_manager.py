"""Module for the hotel manager"""
# pylint: disable=import-error
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from uc3m_travel.json_parser import JsonParser
from storage.reservation_json_store import ReservationJsonStore
from storage.stay_json_store import StayJsonStore


# pylint: disable=too-few-public-methods
class HotelManager:
    """Class with all the methods for managing reservations and stays"""

    # pylint: disable=invalid-name
    class __HotelManager:

        # pylint: disable=too-many-arguments
        def room_reservation(self,
                             credit_card: str,
                             name_surname: str,
                             id_card: str,
                             phone_number: str,
                             room_type: str,
                             arrival_date: str,
                             num_days: int) -> str:
            """manges the hotel reservation: creates a reservation and saves it into a json file"""
            my_reservation = HotelReservation(id_card=id_card,
                                              credit_card_number=credit_card,
                                              name_surname=name_surname,
                                              phone_number=phone_number,
                                              room_type=room_type,
                                              arrival=arrival_date,
                                              num_days=num_days)

            json_store_res = ReservationJsonStore()
            if json_store_res.find_item("_HotelReservation__localizer", my_reservation.localizer):
                raise HotelManagementException("Reservation already exists")

            if json_store_res.find_item("_HotelReservation__id_card", my_reservation.id_card):
                raise HotelManagementException("This ID card has another reservation")

            json_store_res.add_item(my_reservation)
            return my_reservation.localizer

        def guest_arrival(self, file_input: str) -> str:
            """manages the arrival of a guest with a reservation"""
            my_id_card, my_localizer = JsonParser(file_input).parse("Error: file input not found")
            my_checkin = HotelStay(my_id_card, my_localizer)
            stay_json_store = StayJsonStore()
            if stay_json_store.find_item("_HotelStay__room_key", my_checkin.room_key):
                raise HotelManagementException("ckeckin  ya realizado")
            stay_json_store.add_item(my_checkin)
            return my_checkin.room_key

        def guest_checkout(self, room_key: str) -> bool:
            """manages the checkout of a guest"""
            HotelStay.get_stay_from_room_key(room_key)
            HotelStay.check_out(room_key)
            return True

    __instance = None

    def __new__(cls):
        if not HotelManager.__instance:
            HotelManager.__instance = HotelManager.__HotelManager()
        return HotelManager.__instance
