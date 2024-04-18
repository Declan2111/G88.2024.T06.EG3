import re
from attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException


class ArrivalDate(Attribute):

    def __init__(self, attr_value):
        super().__init__()
        self._validation_pattern = r"^(([0-2]\d|-3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$"
        self._error_message = "Invalid date format"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        return super()._validate(attr_value)



