from model.store import Store
from view.view import View
from view.user.list_users_view import ListUsersView
from view.user.delete_user_view import DeleteUserView
from view.shell_builder import ShellBuilder


class ManageUsersView(View):
    """
    Interface used by admin to manage articles
    """

    def __init__(self, store: Store):
        self._store = store

    def show(self):
        shell = ShellBuilder(prompt="users") \
            .add_command('list', 'Show users', ListUsersView(self._store)) \
            .add_command('delete', 'Delete user', DeleteUserView(self._store))
        shell.show()
