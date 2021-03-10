from exceptions import InvalidData


class CommandManager:

    def __init__(self, command):
        self._command = command

    def deliver(self):
        # check status ...
        if self._command.status == 'delivered':
            raise InvalidData()

        self._command.status = 'delivered'

    def cancel(self):
        self._command.status = 'cancelled'
