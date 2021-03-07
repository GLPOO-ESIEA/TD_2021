from model.dao.dao_error_handler import dao_error_handler

from model.mapping.admin import Admin
from model.dao.user_dao import UserDAO


class AdminDAO(UserDAO):
    """
    Admin Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    @dao_error_handler
    def get_all(self):
        query = self._database_session.query(Admin).order_by(Admin.firstname)
        return query.all()
