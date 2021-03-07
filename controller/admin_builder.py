from controller.user_builder import UserBuilder
from controller.validation.user_validation import UserValidation
from model.mapping.admin import Admin
from exceptions import Error


class AdminBuilder(UserBuilder):
    """
    admin actions
    """

    def create_user(self, username: str, firstname: str, lastname: str, email: str):
        try:
            # Save user in database
            admin = Admin(username, firstname, lastname, email)
            UserValidation(admin).validate()
            self._db_session.session.add(admin)
            return admin
        except Error as e:
            # log error
            raise e
