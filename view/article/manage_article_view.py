from view.view import View
from model.store import Store
from view.article.list_article_view import ListArticleView
from view.article.article_view import AddArticleView, DeleteArticleView, UpdateArticleView
from view.shell_builder import ShellBuilder


class ManageArticleView(View):
    """
    Interface used by admin to manage articles
    """

    def __init__(self, store: Store):
        self._store = store

    def show(self):
        shell = ShellBuilder(prompt="article") \
            .add_command('list', 'Show articles', ListArticleView(self._store)) \
            .add_command('add', 'Add article', AddArticleView(self._store))\
            .add_command('delete', 'Delete article', DeleteArticleView(self._store))\
            .add_command('update', 'Update article', UpdateArticleView(self._store))
        shell.show()
