from view.view import View
from model.store import Store
from view.command.list_commands_view import ListCommandsView

from controller.command_manager import CommandManager

from exceptions import ResourceNotFound, Error, InvalidData


class ManageCommandsView(View):

    def __init__(self, store: Store):
        self._store = store

    def show(self):
        print("Manage commands")
        self.help()
        while True:
            try:
                command = input('commands > ').lower().strip()
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'help':
                    self.help()
                elif command == 'list':
                    ListCommandsView(self._store).show()
                elif command == 'pending':
                    ListCommandsView(self._store, status='pending').show()
                elif command.startswith('deliver ') or command.startswith('cancel '):
                    if len(command.split(' ')) != 2:
                        print("Error with arguments")
                    else:
                        status, command_id = command.split(' ')
                        try:
                            command = self._store.command().get(command_id)
                        except ResourceNotFound:
                            print("Command %s not found" % command_id)
                            continue
                        command_manager = CommandManager(command)
                        if status == 'deliver':
                            command_manager.deliver()
                        elif status == 'cancel':
                            command_manager.cancel()
                        print("Command %s %s" % (command.id, command.status))
                elif command.startswith('user '):
                    if len(command.split(' ')) != 2:
                        print("Error with arguments")
                    else:
                        _, username = command.split(' ')
                        try:
                            user = self._store.customer().get_by_username(username)
                        except ResourceNotFound:
                            print("User %s not found" % username)
                            continue
                        ListCommandsView(self._store, user=user).show()
                else:
                    print("Unknown command")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))

    def help(self):
        print()
        print("  * deliver <command id>: Update status command to delivered")
        print("  * cancel <command id>: Cancel command")
        print("  * exit: Cancel command")
        print("  * help: show this help")
        print("  * list: List commands")
        print("  * pending: List pending commands")
        print("  * user <username>: List user commands")
        print()
