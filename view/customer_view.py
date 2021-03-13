from model.mapping.customer import Customer
from model.store import Store
from view.common import Common
from view.view import View
from view.article.list_article_view import ListArticleView
from view.shell_builder import ShellBuilder
from view.command.command_view import CommandView
from view.command.list_commands_view import ListCommandsView


class CustomerView(View):
    """
    Customer View
    Customers interface
    """

    def __init__(self, customer: Customer, store: Store):
        self._common = Common()
        self._customer = customer
        self._store = store

    def show(self):
        shell = ShellBuilder() \
            .add_command('articles', 'Show articles', ListArticleView(self._store)) \
            .add_command('command', 'Create command', CommandView(self._customer, self._store))\
            .add_command('commands', 'List historic commands', ListCommandsView(self._store, self._customer))\
            .add_command('profile', 'Show user profile', View())
        shell.show()
