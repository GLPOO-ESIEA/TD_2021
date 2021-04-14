from model.dao.admin_dao import AdminDAO
from model.dao.customer_dao import CustomerDAO
from model.dao.user_dao import UserDAO


class Store:

    def __init__(self, db_session):
        self._db_session = db_session

    def admin(self):
        return AdminDAO(self._db_session)

    def customer(self):
        return CustomerDAO(self._db_session)

    def user(self):
        return UserDAO(self._db_session)
