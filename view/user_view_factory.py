from model.mapping.user import User
from controller.customer_controller import CustomerController
from view.customer_view import CustomerView
from exceptions import Error


class UserViewFactory:

    def __init__(self, user: User):
        self._user = user

    def show(self):
        if self._user.user_type == 'customer':
            return CustomerView(CustomerController(self._user)).show()
        elif self._user.user_type == 'admin':
            raise NotImplementedError()
        raise Error()
