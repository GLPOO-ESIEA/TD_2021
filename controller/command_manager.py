from model.dao.command_dao import CommandDAO
from exceptions import InvalidData


class CommandManager:

    def __init__(self, command, db_session):
        self._command = command
        self._db_session = db_session

    def update_status(self, status):
        # check status ...
        if self._command.status == 'terminated':
            raise InvalidData()

        self._command.status = status
        self._db_session.flush()
