from model.dao.user_dao import UserDAO
from controller.customer_controller import CustomerController
from controller.customer_builder import CustomerBuilder
from vue.common import Common


class MainVue:

    def __init__(self, user_dao: UserDAO):
        self._user_dao = user_dao
        self._common = Common()

    def main(self):
        is_member = self._common.query_yes_no("Are you already a member ?")
        if is_member:
            self.connect()
        else:
            self.subscribe()

    def connect(self):
        pass

    def subscribe(self):
        # Show subscription formular
        customer_builder = CustomerBuilder(self._user_dao)
        print("Store user Subscription")
        print()

        while True:
            username = self._common.ask_name(key_name="username")
            if customer_builder.check_username_exists(username):
                print("/!\\ Customer %s already exists")
            else:
                break
        firstname = self._common.ask_name(key_name="firstname")
        lastname = self._common.ask_name(key_name="lastname")
        email = self._common.ask_email()
        user = customer_builder.create_user(username, firstname, lastname, email)
        self.show_customer_view(user)

    def show_customer_view(self, customer):
        pass

