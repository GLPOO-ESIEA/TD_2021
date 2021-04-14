from model.mapping.customer import Customer
from model.store import Store
from view.common import Common
from view.view import View
from view.shell_builder import ShellBuilder
from view.user.profile_view import ProfileView


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
            .add_command('profile', 'Show user profile', ProfileView(self._store, self._customer))
        shell.show()
