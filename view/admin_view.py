from view.view import View
from view.shell_builder import ShellBuilder
from view.common import Common
from view.list_article_view import ArticleView


class AdminView(View):
    """
    Admin View
    Admin specific interfaces
    """

    def __init__(self, admin_controller):
        self._common = Common()
        self._customer_controller = customer_controller
        self._article_view = article_view

    def show(self):
        shell = ShellBuilder() \
            .add_command('articles', 'Show articles', self._article_view) \
            .add_command('commands', 'List commands', View)\
            .add_command('add_admin', 'Create new admin', View)
        shell.show()
