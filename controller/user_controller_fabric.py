from controller.admin_controller import AdminController
from controller.customer_controller import CustomerController
from controller.user_controller import UserController


class UserControllerFabric:

    def __init__(self, database_session):
        self._database_session = database_session

    def get_controller(self, user_type=None):
        if user_type is None:
            return UserController(self._database_session)

        if user_type == 'customer':
            return CustomerController(self._database_session)
        elif user_type == 'admin':
            return AdminController(self._database_session)
        else:
            return UserController(self._database_session)
