from model.dao.user_dao import UserDAO
from model.dao.member_dao import MemberDAO
from model.dao.coach_dao import CoachDAO


class UserDAOFabric:

    def __init__(self, db_session):
        self._db_session = db_session

    def get_dao(self, type=None):
        if type is None:
            return UserDAO(self._db_session)

        if type == 'customer':
            return MemberDAO(self._db_session)
        elif type == 'admin':
            return CoachDAO(self._db_session)
        else:
            return UserDAO(self._db_session)
