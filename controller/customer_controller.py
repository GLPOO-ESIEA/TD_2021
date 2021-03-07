
from controller.user_controller import UserController
from model.mapping.customer import Customer
from exceptions import Error


class CustomerController(UserController):
    """
    customer actions
    """

    def create_user(self, username: str, firstname: str, lastname: str, email: str):
        try:
            # Save user in database
            customer = Customer(username, firstname, lastname, email)
            self._check_user(customer)
            self._db_session.add(customer)
            return customer
        except Error as e:
            # log error
            raise e
