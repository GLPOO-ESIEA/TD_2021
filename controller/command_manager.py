from model.dao.command_dao import CommandDAO
from exceptions import InvalidData


class CommandManager:

    def __init__(self, command_id, database_engine):
        self._command_id = command_id
        self._database_engine = database_engine

    def update_status(self, status):
        with self._database_engine.new_session() as session:
            command = CommandDAO(session).get(self._command_id)
            # check status ...
            if command.status == 'terminated':
                raise InvalidData()

            command.status = status
