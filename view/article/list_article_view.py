from model.store import Store
from view.view import View


class ListArticleView(View):

    def __init__(self, store: Store, search: str = None):
        self._store = store
        self._search = search

    def show(self):
        if self._search is not None:
            articles = self._store.article().search(self._search)
        else:
            articles = self._store.article().get_all()
        print("Article:")
        for article in articles:
            print("- %s: %s" % (article.name, article.description))
            print("     price: %d" % article.price)
            print("     items: %d" % article.number)
