"""Module for the hotel manager"""
import re
import json
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from freezegun import freeze_time

from attributes.attribute_card_num import CardNum

from attributes.attribute_room_type import RoomType

from attributes.attribute_arrival_date import ArrivalDate

from attributes.attribute_phone_num import PhoneNumber

from attributes.attribute_num_days import NumDays

from attributes.attribute_id import IDNum

from attributes.attribute_localizer import Localizer

from attributes.attribute_roomkey import RoomKey


class HotelManager:
    """Class with all the methods for managing reservations and stays"""
    def __init__(self):
        pass

    def read_data_from_json(self, fi):
        """reads the content of a json file with two fields: CreditCard and phoneNumber"""

        json_data = self.generate_key_list(fi)
        try:
            c = json_data["CreditCard"]
            p = json_data["phoneNumber"]
            req = HotelReservation(id_card="12345678Z",
                                   credit_card_number=c,
                                   name_surname="John Doe",
                                   phone_number=p,
                                   room_type="single",
                                   num_days=3,
                                   arrival="20/01/2024")
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        card_num = CardNum(c)
        if not card_num._validate(c):
            raise HotelManagementException("Invalid credit card number")
        # Close the file
        return req

    # pylint: disable=too-many-arguments
    def room_reservation(self,
                         credit_card:str,
                         name_surname:str,
                         id_card:str,
                         phone_number:str,
                         room_type:str,
                         arrival_date: str,
                         num_days:int)->str:
        """manges the hotel reservation: creates a reservation and saves it into a json file"""

        arrival_date, credit_card, num_days, phone_number, room_type = self.validate_data_room_res(arrival_date,
                                                                                                   credit_card, id_card,
                                                                                                   name_surname,
                                                                                                   num_days,
                                                                                                   phone_number,
                                                                                                   room_type)

        my_reservation = HotelReservation(id_card=id_card,
                                          credit_card_number=credit_card,
                                          name_surname=name_surname,
                                          phone_number=phone_number,
                                          room_type=room_type,
                                          arrival=arrival_date,
                                          num_days=num_days)

        # escribo el fichero Json con todos los datos
        file_store = JSON_FILES_PATH + "store_reservation.json"

        #leo los datos del fichero si existe , y si no existe creo una lista vacia


        data_list = self.generate_key_list(file_store)

        #compruebo que esta reserva no esta en la lista
        for item in data_list:
            if my_reservation.localizer == item["_HotelReservation__localizer"]:
                raise HotelManagementException ("Reservation already exists")
            if my_reservation.id_card == item["_HotelReservation__id_card"]:
                raise HotelManagementException("This ID card has another reservation")
        #añado los datos de mi reserva a la lista , a lo que hubiera
        data_list.append(my_reservation.__dict__)

        #escribo la lista en el fichero
        self.dump_or_NF(file_store, data_list)

        return my_reservation.localizer

    def validate_data_room_res(self, arrival_date, credit_card, id_card, name_surname, num_days, phone_number,
                               room_type):
        r = r'^[0-9]{8}[A-Z]{1}$'
        self.regex_match(id_card, r)
        validate_room = RoomType(room_type)
        room_type = validate_room._validate(room_type)
        r = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
        myregex = re.compile(r)
        regex_matches = myregex.fullmatch(name_surname)
        if not regex_matches:
            raise HotelManagementException("Invalid name format")
        card_num = CardNum(credit_card)
        credit_card = card_num._validate(credit_card)
        validate_arrival = ArrivalDate(arrival_date)
        arrival_date = validate_arrival._validate(arrival_date)
        valid_num_days = NumDays(num_days)
        num_days = valid_num_days._validate(num_days)
        validate_phone = PhoneNumber(phone_number)
        phone_number = validate_phone._validate(phone_number)
        return arrival_date, credit_card, num_days, phone_number, room_type

    def regex_match(self, id_card, r):
        my_regex = re.compile(r)
        if not my_regex.fullmatch(id_card):
            raise HotelManagementException("Invalid IdCard format")
        valid_id = IDNum(id_card)

        if not valid_id._validate(id_card):
            raise HotelManagementException("Invalid IdCard letter")

    def guest_arrival(self, file_input:str)->str:
        """manages the arrival of a guest with a reservation"""
        my_id_card, my_localizer = self.validate_data_guest_arr(file_input)

        reservation_days, reservation_room_type = self.check_file_manip(my_id_card, my_localizer)

        # genero la room key para ello llamo a Hotel Stay
        my_checkin = HotelStay(idcard=my_id_card, numdays=int(reservation_days),
                               localizer=my_localizer, roomtype=reservation_room_type)

        #Ahora lo guardo en el almacen nuevo de checkin
        # escribo el fichero Json con todos los datos
        file_store = JSON_FILES_PATH + "store_check_in.json"

        # leo los datos del fichero si existe , y si no existe creo una lista vacia
        room_key_list = self.generate_key_list(file_store)

        # comprobar que no he hecho otro ckeckin antes
        for item in room_key_list:
            if my_checkin.room_key == item["_HotelStay__room_key"]:
                raise HotelManagementException ("ckeckin  ya realizado")

        #añado los datos de mi reserva a la lista , a lo que hubiera
        room_key_list.append(my_checkin.__dict__)

        self.dump_or_NF(file_store, room_key_list)

        return my_checkin.room_key

    def check_file_manip(self, my_id_card, my_localizer):
        # buscar en almacen
        file_store = JSON_FILES_PATH + "store_reservation.json"
        store_list = self.load_json(file_store, "Error: store reservation not found")
        # compruebo si esa reserva esta en el almacen
        found = False
        for item in store_list:
            if my_localizer == item["_HotelReservation__localizer"]:
                reservation_days = item["_HotelReservation__num_days"]
                reservation_room_type = item["_HotelReservation__room_type"]
                reservation_date_timestamp = item["_HotelReservation__reservation_date"]
                reservation_credit_card = item["_HotelReservation__credit_card_number"]
                reservation_date_arrival = item["_HotelReservation__arrival"]
                reservation_name = item["_HotelReservation__name_surname"]
                reservation_phone = item["_HotelReservation__phone_number"]
                reservation_id_card = item["_HotelReservation__id_card"]
                found = True
        if not found:
            raise HotelManagementException("Error: localizer not found")
        if my_id_card != reservation_id_card:
            raise HotelManagementException("Error: Localizer is not correct for this IdCard")
        # regenrar clave y ver si coincide
        reservation_date = datetime.fromtimestamp(reservation_date_timestamp)
        with freeze_time(reservation_date):
            new_reservation = HotelReservation(credit_card_number=reservation_credit_card,
                                               id_card=reservation_id_card,
                                               num_days=reservation_days,
                                               room_type=reservation_room_type,
                                               arrival=reservation_date_arrival,
                                               name_surname=reservation_name,
                                               phone_number=reservation_phone)
        if new_reservation.localizer != my_localizer:
            raise HotelManagementException("Error: reservation has been manipulated")
        # compruebo si hoy es la fecha de checkin
        reservation_format = "%d/%m/%Y"
        date_obj = datetime.strptime(reservation_date_arrival, reservation_format)
        if date_obj.date() != datetime.date(datetime.utcnow()):
            raise HotelManagementException("Error: today is not reservation date")
        return reservation_days, reservation_room_type

    def validate_data_guest_arr(self, file_input):
        input_list = self.load_json(file_input, "Error: file input not found")
        # comprobar valores del fichero
        try:
            my_localizer = input_list["Localizer"]
            my_id_card = input_list["IdCard"]
        except KeyError as e:
            raise HotelManagementException("Error - Invalid Key in JSON") from e
        r = r'^[0-9]{8}[A-Z]{1}$'
        self.regex_match(my_id_card, r)
        validate_localizer = Localizer(my_localizer)
        validate_localizer._validate(my_localizer)
        return my_id_card, my_localizer

    def generate_key_list(self, file_store):
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                room_key_list = json.load(file)
        except FileNotFoundError as ex:
            room_key_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return room_key_list

    def load_json(self, file_input, message):
        try:
            with open(file_input, "r", encoding="utf-8", newline="") as file:
                input_list = json.load(file)
        except FileNotFoundError as ex:
            raise HotelManagementException(message) from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return input_list


    def dump_or_NF(self, file_store, room_key_list):
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(room_key_list, file, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file  or file path") from ex

    def guest_checkout(self, room_key:str)->bool:
        """manages the checkout of a guest"""
        self.check_departure_data_valid(room_key)

        file_store_checkout = JSON_FILES_PATH + "store_check_out.json"
        room_key_list = self.generate_key_list(file_store_checkout)

        for checkout in room_key_list:
            if checkout["room_key"] == room_key:
                raise HotelManagementException("Guest is already out")

        room_checkout={"room_key":  room_key, "checkout_time":datetime.timestamp(datetime.utcnow())}

        room_key_list.append(room_checkout)

        self.dump_or_NF(file_store_checkout, room_key_list)

        return True

    def check_departure_data_valid(self, room_key):
        validate_room_key = RoomKey(room_key)
        validate_room_key._validate(room_key)
        # check thawt the roomkey is stored in the checkins file
        file_store = JSON_FILES_PATH + "store_check_in.json"
        room_key_list = self.load_json(file_store, "Error: store checkin not found")
        # comprobar que esa room_key es la que me han dado
        found = False
        for item in room_key_list:
            if room_key == item["_HotelStay__room_key"]:
                departure_date_timestamp = item["_HotelStay__departure"]
                found = True
        if not found:
            raise HotelManagementException("Error: room key not found")
        today = datetime.utcnow().date()
        if datetime.fromtimestamp(departure_date_timestamp).date() != today:
            raise HotelManagementException("Error: today is not the departure day")