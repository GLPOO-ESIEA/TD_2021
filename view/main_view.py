from model.store import Store
from controller.customer_controller import CustomerController
from view.common import Common
from view.view import View
from exceptions import ResourceNotFound, InvalidData, Conflict
from view.user_view_factory import UserViewFactory


class MainView(View):

    def __init__(self, store: Store):
        self._store = store
        self._common = Common()

    def show(self):
        is_member = self._common.query_yes_no("Are you already a member ?")
        if is_member:
            return self.connect()
        else:
            return self.subscribe()

    def connect(self):
        print("Connection")
        while True:
            username = self._common.ask_name(key_name="username")
            try:
                user = self._store.user().get_by_username(username)
                break
            except ResourceNotFound:
                print("/!\\ Customer %s not exists" % username)
        UserViewFactory(user, self._store).show()

    def subscribe(self):
        # Show subscription formular
        customer_controller = CustomerController(self._store)
        print("Store user Subscription")
        print()

        try:
            while True:
                # while username found in database, ark username again
                username = self._common.ask_name(key_name="username")
                try:
                    customer_controller.set_username(username)
                    break
                except Conflict as e:
                    print("/!\\ %s" % str(e))
            firstname = self._common.ask_name(key_name="firstname")
            customer_controller.set_firstname(firstname)
            lastname = self._common.ask_name(key_name="lastname")
            customer_controller.set_lastname(lastname)
            email = self._common.ask_email()
            customer_controller.set_email(email)

            user = customer_controller.register()
        except InvalidData as e:
            print("/!\\ %s" % str(e))
            return
        UserViewFactory(user, self._store).show()
