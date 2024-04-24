from attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException
import re


class RoomKey(Attribute):
    """Definition of attribute room key"""

    # pylint: disable+super-init-not-called, too-few-public-methods
    def __init__(self, attr_value):
        """Definition of the attribute RoomKey init"""
        self._validation_pattern = r'^[a-fA-F0-9]{64}$'
        self._error_message = "Invalid room key format"
        self._attr_value = self.validate(attr_value)

    def validate(self, attr_value):
        return super()._validate(attr_value)

