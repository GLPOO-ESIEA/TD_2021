from exceptions import ResourceNotFound, Error, InvalidData, Exit
from view.view import View


class ShellBuilder(View):
    """
    Shell builder
    Used to create easy shell. User must register commands and run show function add end
    """

    def __init__(self, prompt=""):
        self._commands = {
            "help": {"description": "Show help", "view": View()},
            "exit": {"description": "Exit", "view": View()}
        }  # command mapping
        self._prompt = prompt

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

        command = input("%s > " % self._prompt).lower().strip()
        while command not in self._commands.keys():
            print("Unknown command")
            command = input("%s > " % self._prompt).lower().strip()

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
            except Exit:
                raise
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
