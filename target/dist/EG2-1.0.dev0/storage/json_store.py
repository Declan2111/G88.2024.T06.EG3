import hashlib
import json

from uc3m_travel.hotel_management_exception import HotelManagementException


class JsonStore():
    """Json Store class"""
    _data_list = []
    _file_name = ""

    def __init__(self):
        self._data_list = []
        self._file_name = ""

    # def save_reservation(self, res_data):
    #
    # def save_checkin(self, checkin_data):
    #
    # def save_checkout(self, checkout_data):

    def add_item(self, item):
        """adds an item to a json file"""
        self.data_list.append(item.__dict__)

    def save_list_to_file(self):
        """Saves the data to a file"""
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self.data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file  or file path") from ex

    def load_list_from_file(self):
        """Loads the data from a file"""
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = (json.load(file))
        except FileNotFoundError as ex:
            _data_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return self.data_list

    # def add_item(self, item):

    def find_item(self, key, value):
        """finds an item in the store"""
        #self.load_list_from_file()
        for item in self.data_list:
            if item[key] == value:
                return item
        return None



    @property
    def hash(self):
        """returns the hash of the store for checking further modification"""
        self.load_store()
        return hashlib.md5(self.__str__().encode()).hexdigest()
    @property
    def data_list(self):
        return self._data_list
