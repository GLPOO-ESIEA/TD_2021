from view.view import View
from view.shell_builder import ShellBuilder
from view.user.show_profile_view import ShowProfileView
from view.user.update_profile_view import UpdateProfileView
from view.user.delete_user_view import DeleteUserView
from model.store import Store
from model.mapping.user import User


class ProfileView(View):

    """
    Interface used by user to manage profile data
    """

    def __init__(self, store: Store, user: User):
        self._store = store
        self._user = user

    def show(self):
        shell = ShellBuilder(prompt="profile") \
            .add_command('show', 'Show profile', ShowProfileView(self._user))\
            .add_command('update', 'Update profile', UpdateProfileView(self._store, self._user))\
            .add_command('unsubscribe', 'Delete my account', DeleteUserView(self._store, self._user,
                                                                            exit_if_success=True))
        shell.show()
