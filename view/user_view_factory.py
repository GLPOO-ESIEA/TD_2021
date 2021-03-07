from model.mapping.user import User
from controller.customer_controller import CustomerController
from view.customer_view import CustomerView
from exceptions import Error
from model.database import Session


class UserViewFactory:

    def __init__(self, user: User, db_session: Session):
        self._user = user
        self._db_session = db_session

    def show(self):
        if self._user.user_type == 'customer':
            return CustomerView(CustomerController(self._user), self._db_session).show()
        elif self._user.user_type == 'admin':
            raise NotImplementedError()
        raise Error()
