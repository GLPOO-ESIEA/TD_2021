from model.store import Store
from model.mapping.customer import Customer
from controller.user_controller import UserController


class CustomerController(UserController):
    """
    customer create
    """

    def __init__(self, store: Store):
        super().__init__(store)

    def register(self):
        user = Customer(id=self._id,
                        username=self._username,
                        firstname=self._firstname,
                        lastname=self._lastname,
                        email=self._email)
        if self._id is None:
            self._store.user().create(user)
            self._id = user.id
        else:
            self._store.user().update(user)
        return user
