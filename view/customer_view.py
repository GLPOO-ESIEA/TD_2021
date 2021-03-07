from view.common import Common
from view.view import View
from view.list_article_view import ListArticleView
from view.shell_builder import ShellBuilder
from controller.customer_controller import CustomerController
from model.database import Session


class CustomerView(View):
    """
    Customer View
    Members interface features
    """

    def __init__(self, customer_controller: CustomerController, db_session: Session):
        self._common = Common()
        self._customer_controller = customer_controller
        self._db_session = db_session

    def show(self):
        shell = ShellBuilder() \
            .add_command('articles', 'Show articles', ListArticleView(self._db_session)) \
            .add_command('commands', 'List historic commands', View)\
            .add_command('profile', 'Show user profile', View)
        shell.show()
