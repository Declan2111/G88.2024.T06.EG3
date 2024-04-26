"""Contains the class for phone number attribute"""
# pylint: disable=import-error
from attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class PhoneNumber(Attribute):
    """Definition of attribute phone number"""

    # pylint: disable=super-init-not-called, too-few-public-methods
    def __init__(self, attr_value):
        """Definition of the attribute PhoneNumber init"""
        self._validation_pattern = r"^(\+)[0-9]{9}"
        self._error_message = "Invalid phone number format"
        self._attr_value = self._validate(attr_value)
