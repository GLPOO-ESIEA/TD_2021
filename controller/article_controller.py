from model.mapping.article import Article
from model.store import Store
from exceptions import ResourceNotFound, Conflict


class ArticleController:
    """
    article actions
    """

    def __init__(self, store: Store):
        self._store = store
        self._id = None
        self._name = None
        self._price = None
        self._number = None
        self._description = None
        self._article_type = None

    def from_article(self, article: Article):
        self._id = article.id
        self._name = article.name
        self._price = article.price
        self._number = article.number
        self._description = article.description
        self._article_type = article.article_type

    def set_name(self, name):
        # check name not exists
        if self._name != name:
            try:
                self._store.article().get_by_name(name)
                raise Conflict("Article %s already exists" % name)
            except ResourceNotFound:
                self._name = name

    def get_name(self):
        return self._name

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    def set_article_type(self, article_type):
        self._article_type = article_type

    def get_article_type(self):
        return self._article_type

    def set_number(self, number):
        self._number = number

    def get_number(self):
        return self._number

    def register(self):
        article = Article(id=self._id,
                          name=self._name,
                          price=self._price,
                          number=self._number,
                          description=self._description,
                          article_type=self._article_type)
        if self._id is None:
            self._store.article().create(article)
            self._id = article.id
        else:
            self._store.article().update(article)
        return article

