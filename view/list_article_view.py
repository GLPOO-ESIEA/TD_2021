from model.store import Store
from view.view import View


class ListArticleView(View):

    def __init__(self, store: Store):
        self._store = store

    def show(self):
        articles = self._store.article().get_all()
        print("Article:")
        for article in articles:
            print("- %s: %s" % (article.name, article.description))
            print("     price: %d" % article.price)
            print("     items: %d" % article.number)
