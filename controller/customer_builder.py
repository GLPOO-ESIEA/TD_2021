from model.mapping.customer import Customer
from model.store import Store
from controller.validation.user_validation import UserValidation


class CustomerBuilder:
    """
    customer create
    """

    def __init__(self, store: Store):
        self._store = store

    def create_user(self, username: str, firstname: str, lastname: str, email: str):

        # Save user in database
        customer = Customer(username=username,
                            firstname=firstname,
                            lastname=lastname,
                            email=email)
        UserValidation(customer).validate()
        self._store.user().create(customer)
        return customer
