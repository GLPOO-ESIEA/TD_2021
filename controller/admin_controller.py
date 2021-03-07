import re

from controller.user_controller import UserController
from model.mapping.admin import Admin
from exceptions import Error


class AdminController(UserController):
    """
    admin actions
    """

    def create_user(self, username: str, firstname: str, lastname: str, email: str):
        try:
            # Save user in database
            admin = Admin(username, firstname, lastname, email)
            self._check_user(admin)
            self._db_session.session.add(admin)
            return admin
        except Error as e:
            # log error
            raise e
