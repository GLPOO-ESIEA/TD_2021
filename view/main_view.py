from model.dao.user_dao import UserDAO
from controller.customer_builder import CustomerBuilder
from view.common import Common
from view.view import View
from exceptions import ResourceNotFound
from view.user_view_factory import UserViewFactory


class MainView(View):

    def __init__(self, db_session):
        self._user_dao = UserDAO(db_session)
        self._common = Common()
        self._db_session = db_session

    def show(self):
        is_member = self._common.query_yes_no("Are you already a member ?")
        if is_member:
            self.connect()
        else:
            self.subscribe()

    def connect(self):
        print("Connection")
        while True:
            username = self._common.ask_name(key_name="username")
            try:
                user = self._user_dao.get_by_username(username)
                break
            except ResourceNotFound():
                print("/!\\ Customer %s not exists" % username)
        UserViewFactory(user, self._db_session).show()

    def subscribe(self):
        # Show subscription formular
        customer_builder = CustomerBuilder(self._user_dao)
        print("Store user Subscription")
        print()

        while True:
            username = self._common.ask_name(key_name="username")
            try:
                self._user_dao.get_by_username(username)
                print("/!\\ Customer %s already exists" % username)
            except ResourceNotFound:
                break
        firstname = self._common.ask_name(key_name="firstname")
        lastname = self._common.ask_name(key_name="lastname")
        email = self._common.ask_email()
        user = customer_builder.create_user(username, firstname, lastname, email)
        UserViewFactory(user, self._db_session).show()
