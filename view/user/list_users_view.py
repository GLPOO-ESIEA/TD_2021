from model.store import Store
from view.view import View


class ListUsersView(View):
    """
    Show users
    """

    def __init__(self, store: Store):
        self._store = store

    def show(self):
        users = self._store.user().get_all()
        print("Users:")
        for user in users:
            print("- %s: %s" % (user.username, user.user_type))
            print("     firstname: %s" % user.firstname)
            print("     lastname: %s" % user.lastname)
            print("     email: %s" % user.email)
