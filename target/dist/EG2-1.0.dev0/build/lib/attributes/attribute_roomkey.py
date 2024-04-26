"""Contains the class for the room key attribute"""
# pylint: disable=import-error
from attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class RoomKey(Attribute):
    """Definition of attribute room key"""

    # pylint: disable=super-init-not-called
    def __init__(self, attr_value):
        """Definition of the attribute RoomKey init"""
        self._validation_pattern = r'^[a-fA-F0-9]{64}$'
        self._error_message = "Invalid room key format"
        self._attr_value = self._validate(attr_value)
