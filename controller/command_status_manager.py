from exceptions import InvalidData
from model.mapping.command_status_enum import CommandStatusEnum


class CommandStatusManager:
    """
    Manage command Status
    """

    def __init__(self, command):
        self._command = command

    def deliver(self):
        # check status ...
        if self._command.status != CommandStatusEnum.PENDING:
            raise InvalidData()

        self._command.status = CommandStatusEnum.DELIVERED

    def cancel(self):
        self._command.status = CommandStatusEnum.CANCELLED
