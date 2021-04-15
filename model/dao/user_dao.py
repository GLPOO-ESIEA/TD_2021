from sqlalchemy import func
from model.dao.dao_error_handler import dao_error_handler
from model.mapping.user import User
from model.dao.dao import DAO
from exceptions import ResourceNotFound


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
    def get_all(self):
        query = self._database_session.query(User).order_by(User.firstname)
        return query.all()

    @dao_error_handler
    def get_by_name(self, firstname: str, lastname: str):
        user = self._database_session.query(User).filter(func.lower(User.firstname) == func.lower(firstname),
                                                         func.lower(User.lastname) == func.lower(lastname))\
            .order_by(User.username).first()
        if user is None:
            raise ResourceNotFound()
        return user

    @dao_error_handler
    def get_by_username(self, username: str):
        return self._database_session.query(User).filter_by(username=username)\
            .order_by(User.username).one()
