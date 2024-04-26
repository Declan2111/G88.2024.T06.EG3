"""Contains class for attribute name and suranme"""
# pylint: disable=import-error
from attributes.attribute import Attribute


# pylint: disable=too-few-public-methods
class NameSur(Attribute):
    """Atrribute call for name and surname"""

    # pylint: disable=super-init-not-called
    def __init__(self, attr_value):
        self._validation_pattern = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
        self._error_message = "Invalid name format"
        self._attr_value = self._validate(attr_value)
