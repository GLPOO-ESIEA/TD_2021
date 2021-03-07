import re

from model.mapping.user import User
from exceptions import InvalidData


class UserController:
    """
    user actions
    """

    def __init__(self, db_session):
        self._db_session = db_session

    def create_user(self, username: str, firstname: str, lastname: str, email: str):
        raise NotImplementedError()

    def update_user(self, user, **user_data):  # **user_data catch all arguments as username=value, lastname=value
        for key in ['username', 'firstname', 'lastname', 'email']:
            if user_data.get(key) is not None:  # Check key is in user_data
                setattr(user, key, user_data['key'])  # update attribute key in user object
        self._db_session.flush()
        return user

    def delete_user(self, user):
        self._db_session.delete(user)

    def _check_user(self, user: User, update=False):
        data = user.to_dict()
        name_pattern = re.compile("^[\S-]{2,50}$")
        type_pattern = re.compile("^(customer|seller)$")
        email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        mandatories = {
            'username': {"type": str, "regex": name_pattern},
            'firstname': {"type": str, "regex": name_pattern},
            'lastname': {"type": str, "regex": name_pattern},
            'email': {"type": str, "regex": email_pattern},
            'type': {"type": str, "regex": type_pattern}
        }
        for mandatory, specs in mandatories.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "type" in specs and not isinstance(value, specs["type"]):
                raise InvalidData("Invalid type %s" % mandatory)
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)
