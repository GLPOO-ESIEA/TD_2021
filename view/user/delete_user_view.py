from view.view import View
from view.common import Common
from model.mapping.user import User
from model.store import Store
from exceptions import Exit


class DeleteUserView(View):

    def __init__(self, store: Store, user: User):
        self._store = store
        self._user = user
        self._common = Common()

    def show(self):
        if self._common.query_yes_no("Are you sure to delete user %s ?" % self._user.username):
            self._store.user().delete(self._user)
            print("User %s deleted" % self._user.username)
            raise Exit("Program exited")
