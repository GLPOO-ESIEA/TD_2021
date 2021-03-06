import re

from model.mapping.user import User
from model.dao.user_dao import UserDAO
from exceptions import Error, InvalidData


class UserController:
    """
    user actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_users(self):
        with self._database_engine.new_session() as session:
            users = UserDAO(session).get_all()
            users_data = [user.to_dict() for user in users]
        return users_data

    def get_user(self, user_id):
        with self._database_engine.new_session() as session:
            user = UserDAO(session).get(user_id)
            user_data = user.to_dict()
        return user_data

    def create_user(self, data):
        raise NotImplementedError()
        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save user in database
                user = User(username=data['username'],
                            firstname=data['firstname'],
                            lastname=data['lastname'],
                            email=data.get('email'))
                session.add(user)
                user_data = user.to_dict()
                return user_data
        except Error as e:
            # log error
            raise e

    def update_user(self, user_id, user_data):

        self._check_profile_data(user_data, update=True)
        with self._database_engine.new_session() as session:
            user_dao = UserDAO(session)
            user = user_dao.get(user_id)
            for key in ['username', 'firstname', 'lastname', 'email']:
                if user_data.get(key) is not None:
                    setattr(user, key, user_data['key'])
            user = session.merge(user)
            return user.to_dict()

    def delete_user(self, user_id):

        with self._database_engine.new_session() as session:
            user_dao = UserDAO(session)
            user = user_dao.get(user_id)
            session.delete(user)

    def search_user(self, firstname, lastname):

        # Query database
        with self._database_engine.new_session() as session:
            user_dao = UserDAO(session)
            user = user_dao.get_by_name(firstname, lastname)
            return user.to_dict()

    def _check_profile_data(self, data, update=False):
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
