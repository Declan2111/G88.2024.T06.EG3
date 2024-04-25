''' Class HotelStay (GE2.2) '''
from datetime import datetime
import hashlib

from attributes.attribute_id import IDNum
from attributes.attribute_localizer import Localizer
from uc3m_travel import HotelReservation

from uc3m_travel.hotel_management_exception import HotelManagementException

from storage.stay_json_store import StayJsonStore

from attributes.attribute_roomkey import RoomKey

from storage.checkout_json_store import CheckoutJsonStore


class HotelStay:
    """Class for representing hotel stays"""
    def __init__(self,
                 idcard: str,
                 localizer: str
                 ):
        """constructor for HotelStay objects"""
        self.__alg = "SHA-256"
        self.__localizer = Localizer(localizer).value
        self.__idcard = IDNum(idcard).value
        reservation = HotelReservation.load_reservation_from_localizer(self.localizer)
        if reservation.id_card != self.__idcard:
            raise HotelManagementException("Error: Localizer is not correct for this IdCard")
        self.__type = reservation.room_type
        #self.__type = roomtype
        justnow = datetime.utcnow()
        self.__arrival = datetime.timestamp(justnow)
        reservation_format = "%d/%m/%Y"
        date_obj = datetime.strptime(reservation.arrival, reservation_format)
        if date_obj.date() != datetime.date(datetime.utcnow()):
            raise HotelManagementException("Error: today is not reservation date")
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express num_days in seconds
        self.__departure = self.__arrival + (reservation.num_days * 24 * 60 * 60)
        self.__room_key = hashlib.sha256(self.__signature_string().encode()).hexdigest()


    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
            ",departure:" + str(self.__departure) + "}"

    @property
    def id_card(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return self.__room_key

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        """returns the value of the departure date"""
        self.__departure = value

    @classmethod
    def get_stay_from_room_key(cls, room_key: str):
        """Creates an instance of the HotelStay class"""

        json_checkout_store = CheckoutJsonStore()
        if json_checkout_store.find_item("room_key", room_key):
            raise HotelManagementException("Guest is already out")

        stay = StayJsonStore()

        stay_info = stay.find_stay_checkout("_HotelStay__room_key", RoomKey(room_key).value)
        print(stay_info)
        if not stay_info:
            raise HotelManagementException("Error: room key not found")
        departure_date = datetime.fromtimestamp(
        stay_info["_HotelStay__departure"])
        today = datetime.utcnow().date()
        if departure_date.date() != today:
            raise HotelManagementException("Error: today is not the departure day")
        return HotelStay


    # def check_out(self):
    #     json_checkout_store = CheckoutJsonStore()
    #     if json_checkout_store.find_item("room_key", room_key):
    #         raise HotelManagementException("Guest is already out")
    #
    #     room_checkout = {"room_key": room_key, "checkout_time": datetime.timestamp(datetime.utcnow())}
    #     json_checkout_store.add_item(room_checkout)
    #     json_checkout_store.save_list_to_file()
