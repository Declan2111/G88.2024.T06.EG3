from attributes.attribute import Attribute


class NameSur(Attribute):

    def __init__(self, attr_value):
        self._validation_pattern = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
        self._error_message = "Invalid name format"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        return super()._validate(attr_value)

