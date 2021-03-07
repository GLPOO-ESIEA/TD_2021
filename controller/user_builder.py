from model.dao.user_dao import UserDAO


class UserBuilder:
    """
    user builder
    """

    def __init__(self, user_dao):
        self._user_dao = user_dao

    def create_user(self, username: str, firstname: str, lastname: str, email: str):
        raise NotImplementedError()
