
from controller.user_builder import UserBuilder
from controller.validation.user_validation import UserValidation
from model.mapping.customer import Customer
from exceptions import Error


class CustomerBuilder(UserBuilder):
    """
    customer actions
    """

    def create_user(self, username: str, firstname: str, lastname: str, email: str):

        # Save user in database
        customer = Customer(username=username,
                            firstname=firstname,
                            lastname=lastname,
                            email=email)
        UserValidation(customer).validate()
        self._store.user().create(customer)
        return customer
