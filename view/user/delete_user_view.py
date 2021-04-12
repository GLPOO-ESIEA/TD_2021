from controller.customer_controller import CustomerController
from model.mapping.user import User
from model.store import Store
from exceptions import Exit, ResourceNotFound
from view.view import View
from view.common import Common


class DeleteUserView(View):

    def __init__(self, store: Store, user: User = None, exit_if_success=False):
        self._store = store
        self._user = user
        self._common = Common()
        self._exit_if_success = exit_if_success

    def show(self):
        if self._user is None:
            # ask user
            username = self._common.ask_name("username")
            try:
                self._user = self._store.user().get_by_username(username)
            except ResourceNotFound:
                print("User %s not found" % username)
                return
        username = self._user.username
        if self._common.query_yes_no("Are you sure to delete user %s ?" % username):
            customer_controller = CustomerController(self._store)
            customer_controller.from_user(self._user)
            customer_controller.delete()
            print("User %s deleted" % username)
            if self._exit_if_success:
                raise Exit("Program exited")
