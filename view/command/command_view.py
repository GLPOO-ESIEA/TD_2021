from view.view import View
from view.common import Common
from view.article.list_article_view import ListArticleView

from model.store import Store
from model.mapping.customer import Customer
from controller.command_builder import CommandBuilder

from exceptions import InvalidData, Error, ResourceNotFound, NotEnoughArticle


class CommandView(View):

    def __init__(self, user: Customer, store: Store):
        self._user = user
        self._store = store
        self._common = Common()
        self._command = CommandBuilder(self._user)

    def show(self):
        print("Create command")
        self.help()
        while True:
            try:
                command = input('command > ').lower().strip()
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'help':
                    self.help()
                elif command == 'register':
                    self._command.register()
                    print("Command registered, it will be take in charge by our team !")
                    break
                elif command == 'price':
                    print("Price: %d euros" % self._command.get_price())
                elif command == 'articles':
                    ListArticleView(self._store).show()
                elif command == 'basket':
                    self.show_basket()
                elif command.startswith('add ') or command.startswith('update '):
                    if len(command.split(' ')) != 3:
                        print("Error with arguments")
                    else:
                        action, article_name, number = command.split(' ')
                        # TODO: check number is integer
                        self.add_article(article_name, int(number), update=action == 'update')
                elif command.startswith('del '):
                    if len(command.split(' ')) != 2:
                        print("Error with arguments")
                    else:
                        _, article_name = command.split(' ')
                        self.delete_article(article_name)
                elif command.startswith('search '):
                    if len(command.split(' ')) != 2:
                        print("Error with arguments")
                    else:
                        _, search = command.split(' ')
                        ListArticleView(self._store, search=search).show()
                else:
                    print("Unknown command")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))

    def add_article(self, article_name: str, number: int, update: bool = False):
        try:
            article = self._store.article().get_by_name(article_name)
        except ResourceNotFound:
            print("Article %s not found" % article_name)
            return

        try:
            if update:
                self._command.update_number(article, number)
                print("Article %s updated" % article_name)
            else:
                self._command.add_article(article, number)
                print("Article %s added" % article_name)
        except NotEnoughArticle:
            print("/!\\ Not enough article in store")

    def delete_article(self, article_name: str):
        try:
            article = self._store.article().get_by_name(article_name)
        except ResourceNotFound:
            print("Article %s not found" % article_name)
            return
        self._command.remove_article(article)
        print("Article %s deleted" % article_name)

    def show_basket(self):
        basket = self._command.get_basket()
        for item in basket:
            print(" * %d x %s (%s)" % (item.number, item.article.name, item.article.description))

    def help(self):
        print()
        print("  * add <article> <number>: Add article in basket")
        print("  * del <article>: Delete article in basket")
        print("  * update <article> <number>: Update number article items")
        print("  * articles: Show articles")
        print("  * basket: Show basket items")
        print("  * exit: Cancel command")
        print("  * help: show this help")
        print("  * price: Show command price")
        print("  * register: Register command")
        print("  * search <string>: Search articles")
        print()
