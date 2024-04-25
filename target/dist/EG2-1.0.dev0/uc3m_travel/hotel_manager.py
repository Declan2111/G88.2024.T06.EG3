"""Module for the hotel manager"""
import json
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay

from storage.reservation_json_store import ReservationJsonStore

from storage.stay_json_store import StayJsonStore

class HotelManager:
    """Class with all the methods for managing reservations and stays"""

    def __init__(self):
        pass

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

        # leo los datos del fichero si existe , y si no existe creo una lista vacia
        json_store_res = ReservationJsonStore()
        if json_store_res.find_item("_HotelReservation__localizer", my_reservation.localizer):
            raise HotelManagementException("Reservation already exists")

        if json_store_res.find_item("_HotelReservation__id_card", my_reservation.id_card):
            raise HotelManagementException("This ID card has another reservation")

        json_store_res.add_item(my_reservation)
        return my_reservation.localizer

    def guest_arrival(self, file_input: str) -> str:
        """manages the arrival of a guest with a reservation"""
        my_id_card, my_localizer = self.validate_data_guest_arr(file_input)
        # genero la room key para ello llamo a Hotel Stay
        my_checkin = HotelStay(my_id_card, my_localizer)
        stay_json_store = StayJsonStore()
        # comprobar que no he hecho otro ckeckin antes
        if stay_json_store.find_item("_HotelStay__room_key", my_checkin.room_key):
            raise HotelManagementException("ckeckin  ya realizado")
        stay_json_store.add_item(my_checkin)
        # añado los datos de mi reserva a la lista , a lo que hubiera
        return my_checkin.room_key

    def validate_data_guest_arr(self, file_input):
        input_list = self.load_json(file_input, "Error: file input not found")
        # comprobar valores del fichero
        try:
            my_localizer = input_list["Localizer"]
            my_id_card = input_list["IdCard"]
        except KeyError as e:
            raise HotelManagementException("Error - Invalid Key in JSON") from e
        return my_id_card, my_localizer

    def load_json(self, file_input, message):
        try:
            with open(file_input, "r", encoding="utf-8", newline="") as file:
                input_list = json.load(file)
        except FileNotFoundError as ex:
            raise HotelManagementException(message) from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return input_list

    def guest_checkout(self, room_key: str) -> bool:
        """manages the checkout of a guest"""
        HotelStay.get_stay_from_room_key(room_key)
        HotelStay.check_out(room_key)
        return True
