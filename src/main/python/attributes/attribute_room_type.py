from attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException

# pylint: disable=too-few-public-methods
class RoomType(Attribute):
    """Definition of attribute room key"""

    def __init__(self, attr_value):
        super().__init__()
        self._validation_pattern = r"(SINGLE|DOUBLE|SUITE)"
        self._error_message = "Invalid roomtype value"
        self._attr_value = self._validate(attr_value)



