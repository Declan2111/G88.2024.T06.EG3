import re
from attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException


class NumDays(Attribute):

    def __init__(self, attr_value):
        self._validation_pattern = r"\b\d{1,2}\b"
        self._error_message = "Invalid num_days datatype"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        super()._validate(str(attr_value))
        if (attr_value < 1 or attr_value > 10):
            raise HotelManagementException("Numdays should be in the range 1-10")
        return attr_value


