from view.common import Common
from view.view import View
from view.list_article_view import ListArticleView
from view.shell_builder import ShellBuilder
from model.mapping.customer import Customer
from model.store import Store


class CustomerView(View):
    """
    Customer View
    Members interface features
    """

    def __init__(self, customer: Customer, store: Store):
        self._common = Common()
        self._customer = customer
        self._store = store

    def show(self):
        shell = ShellBuilder() \
            .add_command('articles', 'Show articles', ListArticleView(self._store)) \
            .add_command('commands', 'List historic commands', View)\
            .add_command('profile', 'Show user profile', View)
        shell.show()
