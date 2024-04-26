"""Contains the child attribute class Localizer"""
# pylint: disable=import-error
from attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class Localizer(Attribute):
    """Contains the attribute Localizer"""

    # pylint: disable=super-init-not-called
    def __init__(self, attr_value):
        self._validation_pattern = r'^[a-fA-F0-9]{32}$'
        self._error_message = "Invalid localizer"
        self._attr_value = self._validate(attr_value)
