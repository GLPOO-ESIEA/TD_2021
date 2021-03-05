from model.mapping.user import User
from view.customer_view import CustomerView
from view.admin_view import AdminView
from exceptions import Error
from model.store import Store


class UserViewFactory:
    """
    From user object, show appropriate view from user type
    Design Pattern factory
    """

    def __init__(self, user: User, store: Store):
        self._user = user
        self._store = store

    def show(self):
        if self._user.user_type == 'customer':
            return CustomerView(self._user, self._store).show()
        elif self._user.user_type == 'admin':
            return AdminView(self._user, self._store).show()
        raise Error()
