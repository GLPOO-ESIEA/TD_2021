from view.view import View
from model.store import Store
from model.mapping.customer import Customer


class ListCommandsView(View):

    def __init__(self, store: Store, user: Customer = None):
        self._store = store
        self._user = user

    def show(self):
        if self._user is not None:
            commands = self._user.commands
        else:
            commands = self._store.command().get_all()
        print()
        print("Commands:")
        print()
        for command in commands:
            articles = command.articles
            custumer = command.customer

            print("* customer: %s" % custumer.username)
            print("  status: %s" % command.status)
            print("  date: %s" % command.date)
            print("  articles: ")
            for item in articles:
                print("   - %s: %d" % (item.article.name, item.number))
        print()
