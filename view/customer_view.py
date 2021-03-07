from view.common import Common
from view.view import View
from view.shell_builder import ShellBuilder
from controller.customer_controller import CustomerController


class CustomerView(View):
    """
    Customer View
    Members interface features
    """

    def __init__(self, customer_controller: CustomerController):
        self._common = Common()
        self._customer_controller = customer_controller

    def show(self):
        shell = ShellBuilder() \
            .add_command('articles', 'Show articles', None) \
            .add_command('commands', 'List historic commands', None)\
            .add_command('profile', 'Show user profile', None)
        shell.show()
