import re

from attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException


class IDNum(Attribute):

    def __init__(self, attr_value):
        self._validation_pattern = r'\b\d{8}[A-Z]\b'
        self._attr_value = self._validate(attr_value)
        self._error_message = "Invalid ID Number"

    def _validate(self, attr_value):
        super()._validate(attr_value)
        valid_chars = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
                       "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
                       "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
                       "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}
        v = int(attr_value[0:8])
        r = str(v % 23)
        if attr_value[8] == valid_chars[r]:
            return attr_value


