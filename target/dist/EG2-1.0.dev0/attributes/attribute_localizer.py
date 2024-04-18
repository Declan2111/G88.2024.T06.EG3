import re

from attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException


class Localizer(Attribute):

    def __init__(self, attr_value):
        self._validation_pattern = r'^[a-fA-F0-9]{32}$'
        self._error_message = "Invalid localizer"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        super()._validate(attr_value)
        r = r'^[a-fA-F0-9]{32}$'
        myregex = re.compile(r)
        if not myregex.fullmatch(attr_value):
            raise HotelManagementException("Invalid localizer")
        return attr_value