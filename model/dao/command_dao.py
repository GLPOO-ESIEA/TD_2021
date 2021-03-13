from model.dao.dao_error_handler import dao_error_handler
from model.mapping.command import Command
from model.mapping.command_status_enum import CommandStatusEnum
from model.dao.dao import DAO


class CommandDAO(DAO):
    """
    User Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    @dao_error_handler
    def get(self, id):
        return self._database_session.query(Command).filter_by(id=id).one()

    @dao_error_handler
    def get_all(self, status: CommandStatusEnum = None):
        query = self._database_session.query(Command).order_by(Command.date)
        if status is not None:
            query = query.filter_by(status=status)
        return query.all()
