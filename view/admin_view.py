from view.view import View
from view.shell_builder import ShellBuilder
from view.common import Common
from model.store import Store
from view.article.manage_article_view import ManageArticleView
from view.command.list_commands_view import ListCommandsView


class AdminView(View):
    """
    Admin View
    Admin specific interfaces
    """

    def __init__(self, admin_controller, store: Store):
        self._common = Common()
        self._admin_controller = admin_controller
        self._store = store

    def show(self):
        shell = ShellBuilder() \
            .add_command('articles', 'Manage articles', ManageArticleView(self._store)) \
            .add_command('commands', 'Manage commands', ListCommandsView(self._store))\
            .add_command('add_admin', 'Create new admin', View)
        shell.show()
