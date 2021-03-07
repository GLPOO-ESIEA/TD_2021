
from controller.user_builder import UserBuilder
from controller.validation.user_validation import UserValidation
from model.mapping.customer import Customer
from exceptions import Error, ResourceNotFound


class CustomerBuilder(UserBuilder):
    """
    customer actions
    """

    def create_user(self, username: str, firstname: str, lastname: str, email: str):
        try:
            # Save user in database
            customer = Customer(username=username,
                                firstname=firstname,
                                lastname=lastname,
                                email=email)
            UserValidation(customer).validate()
            self._user_dao.create(customer)
            return customer
        except Error as e:
            # log error
            raise e

    def check_username_exists(self, username):
        try:
            self._user_dao.get_by_username(username)
            return True
        except ResourceNotFound:
            return False
