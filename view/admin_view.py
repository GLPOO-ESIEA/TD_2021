from view.view import View
from view.shell_builder import ShellBuilder
from view.common import Common
from view.article.manage_article_view import ManageArticleView
from view.command.manage_commands_view import ManageCommandsView

from model.store import Store


class AdminView(View):
    """
    Admin View
    Admin specific interface
    """

    def __init__(self, admin_controller, store: Store):
        self._common = Common()
        self._admin_controller = admin_controller
        self._store = store

    def show(self):
        shell = ShellBuilder() \
            .add_command('articles', 'Manage articles', ManageArticleView(self._store)) \
            .add_command('commands', 'Manage commands', ManageCommandsView(self._store))\
            .add_command('add_admin', 'Create new admin', View())
        shell.show()
