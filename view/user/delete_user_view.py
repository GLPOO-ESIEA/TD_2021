from controller.customer_controller import CustomerController
from model.mapping.user import User
from model.store import Store
from exceptions import Exit
from view.view import View
from view.common import Common


class DeleteUserView(View):

    def __init__(self, store: Store, user: User):
        self._store = store
        self._user = user
        self._common = Common()

    def show(self):
        if self._common.query_yes_no("Are you sure to delete user %s ?" % self._user.username):
            customer_controller = CustomerController(self._store)
            customer_controller.from_user(self._user)
            customer_controller.delete()
            print("User %s deleted" % self._user.username)
            raise Exit("Program exited")
