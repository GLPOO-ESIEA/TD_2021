from exceptions import InvalidData


class CommandManager:

    def __init__(self, command):
        self._command = command

    def update_status(self, status):
        # check status ...
        if self._command.status == 'terminated':
            raise InvalidData()

        self._command.status = status
