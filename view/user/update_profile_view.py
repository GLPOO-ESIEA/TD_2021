from view.view import View
from view.common import Common
from model.mapping.user import User
from model.store import Store
from controller.customer_controller import CustomerController
from exceptions import InvalidData


class UpdateProfileView(View):

    def __init__(self, store: Store, user: User):
        self._store = store
        self._user = user
        self._common = Common()

    def show(self):
        customer_controller = CustomerController(self._store)
        customer_controller.from_user(self._user)

        print("Update profile")
        try:
            username = self._common.ask(key_name="username", default=customer_controller.get_username())
            customer_controller.set_username(username)
            firstname = self._common.ask(key_name="firstname", default=customer_controller.get_firstname())
            customer_controller.set_firstname(firstname)
            lastname = self._common.ask(key_name="lastname", default=customer_controller.get_lastname())
            customer_controller.set_lastname(lastname)
            email = self._common.ask(key_name="email", default=customer_controller.get_email())
            customer_controller.set_email(email)
            customer_controller.register()
        except InvalidData as e:
            print("/!\\ %s" % str())
            return
