from view.view import View
from model.store import Store
from model.mapping.customer import Customer


class ListCommandsView(View):

    def __init__(self, store: Store, user: Customer = None, status: str = None):
        self._store = store
        self._user = user
        self._status = status

    def show(self):
        print()
        if self._user is not None:
            commands = self._user.commands
            print("%s commands:" % self._user.username)
        elif self._status is not None:
            commands = self._store.command().get_by_status(self._status)
            print("Commands with status %s:" % self._status)
        else:
            commands = self._store.command().get_all()
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
