import re
from exceptions import InvalidData


# Interface validation
class Validate:

    def validate(self):
        raise NotImplementedError()

    def _validate_name(self, value: str):
        name_pattern = "^[\S-]{2,50}$"
        self._validate_regex(value, name_pattern)

    def _validate_email(self, value):
        email_pattern = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
        self._validate_regex(value, email_pattern)

    def _validate_regex(self, value: str, regex: str):
        pattern = re.compile(regex)
        if isinstance(value, str) and not re.match(pattern, value):
            raise InvalidData("Invalid value: %s" % value)
