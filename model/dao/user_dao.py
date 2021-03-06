from model.dao.dao_error_handler import dao_error_handler

from model.mapping.user import User
from model.dao.dao import DAO


class UserDAO(DAO):
    """
    User Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    @dao_error_handler
    def get(self, id):
        return self._database_session.query(User).filter_by(id=id).one()

    @dao_error_handler
    def get_all(self, user_type = None):
        query = self._database_session.query(User).order_by(User.firstname)
        if user_type is not None:
            query = query.filter_by(user_type=user_type)
        return query.all()

    @dao_error_handler
    def get_by_name(self, firstname: str, lastname: str):
        return self._database_session.query(User).filter_by(firstname=firstname, lastname=lastname)\
            .order_by(User.username).first()

    @dao_error_handler
    def get_by_username(self, username: str):
        return self._database_session.query(User).filter_by(username=username)\
            .order_by(User.username).one()
