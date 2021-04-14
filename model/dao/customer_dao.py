from model.dao.dao_error_handler import dao_error_handler

from model.mapping.customer import Customer
from model.dao.user_dao import UserDAO


class CustomerDAO(UserDAO):
    """
    Admin Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    @dao_error_handler
    def get_all(self):
        query = self._database_session.query(Customer).order_by(Customer.firstname)
        return query.all()
