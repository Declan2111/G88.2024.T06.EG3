from attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException
import re


class PhoneNumber(Attribute):
    """Definition of attribute phone number"""

    # pylint: disable+super-init-not-called, too-few-public-methods
    def __init__(self, attr_value):
        """Definition of the attribute PhoneNumber init"""
        self._validation_pattern = r"^(\+)[0-9]{9}"
        self._error_message = "Invalid phone number format"
        self._attr_value = self.validate(attr_value)

    def validate(self, attr_value):
        return super()._validate(attr_value)
