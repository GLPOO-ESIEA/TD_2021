from view.view import View
from model.store import Store

from controller.article_controller import ArticleController
from view.common import Common
from exceptions import Conflict, ResourceNotFound
from model.mapping.article import Article


class ArticleView(View):

    def __init__(self, store: Store):
        self._common = Common()
        self._store = store

    def show(self):
        raise NotImplementedError()

    def ask_article(self):
        name = self._common.ask_name(key_name="name")
        try:
            article = self._store.article().get_by_name(name)
            return article
        except ResourceNotFound:
            print("Article %s not found")
            return None

    def formular(self, article: Article = None):
        # Show subscription formular
        article_controller = ArticleController(self._store)
        if article:
            print("Update article")
            article_controller.from_article(article)

        while True:
            name = self._common.ask_name(key_name="name", default=article_controller.get_name())
            try:
                article_controller.set_name(name)
                break
            except Conflict as e:
                print("/!\\ %s" % str(e))
        description = self._common.ask(key_name="description", default=article_controller.get_description())
        article_controller.set_description(description)
        default_value = None
        if article_controller.get_price() is not None:
            default_value = str(article_controller.get_price())
        price = self._common.ask(key_name="price", regex="^\d+(\.\d+)?$",
                                 default=default_value)
        article_controller.set_price(float(price))
        default_value = None
        if article_controller.get_number() is not None:
            default_value = str(article_controller.get_number())
        number = self._common.ask(key_name="number", regex="^\d+$",
                                  default=default_value)
        article_controller.set_number(int(number))
        article_type = self._common.ask_name(key_name="article_type",
                                             default=article_controller.get_article_type())
        article_controller.set_article_type(article_type=article_type)

        article_controller.register()


class AddArticleView(ArticleView):

    def show(self):
        print("Add new article")
        print()
        self.formular()


class UpdateArticleView(ArticleView):

    def show(self):
        print("Update article")
        article = self.ask_article()
        if article is None:
            return
        self.formular(article=article)


class DeleteArticleView(ArticleView):

    def show(self):
        print("Delete article")
        article = self.ask_article()
        if article is None:
            return
        article_name = article.name
        self._store.article().delete(article)
        print("-> Article %s deleted" % article_name)
