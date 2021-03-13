from view.view import View
from model.store import Store
from model.mapping.customer import Customer
from model.mapping.command_status_enum import CommandStatusEnum


class ListCommandsView(View):
    """
    Show commands
    """

    def __init__(self, store: Store, user: Customer = None, status: CommandStatusEnum = None):
        """
        Commands can be filtered by user or status
        """
        self._store = store
        self._user = user
        self._status = status

    def show(self):
        print()
        if self._user is not None:
            commands = self._user.commands
            print("%s commands:" % self._user.username)
        else:
            commands = self._store.command().get_all(status=self._status)
            print("Commands:")
        print()
        for command in commands:
            articles = command.articles
            custumer = command.customer

            print("* customer: %s" % custumer.username)
            print("  identifier: %s" % command.id)
            print("  status: %s" % command.status)
            print("  date: %s" % command.date)
            print("  articles: ")
            for item in articles:
                print("   - %s: %d" % (item.article.name, item.number))
        print()
