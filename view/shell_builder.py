from exceptions import ResourceNotFound, Error, InvalidData
from view.view import View


class ShellBuilder(View):
    """
    Shell builder
    Admin specific interfaces
    """

    def __init__(self):
        self._commands = {
            "help": {"description": "Show help", "view": View},
            "exit": {"description": "Exit", "view": View}
        }  # command mapping

    def add_command(self, command: str, description: str, view: View):
        self._commands[command] = {
            "description": description,
            "view": view
        }
        return self

    def help(self):
        print()
        for command, data in self._commands.items():
            print("  * %s: '%s'" % (command, data['description']))
        print()

    def ask_command(self):

        command = input('command > ').lower().strip()
        while command not in self._commands.keys():
            print("Unknown command")
            command = input('command > ').lower().strip()

        return command

    def show(self):

        self.help()

        while True:
            try:
                command = self.ask_command()
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'help':
                    self.help()
                elif command in self._commands.keys():
                    view = self._commands[command]['view']
                    view.show()
                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
