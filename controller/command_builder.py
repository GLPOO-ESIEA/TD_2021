from model.mapping.article import Article
from exceptions import NotEnoughArticle, ResourceNotFound
from model.mapping.command import Command


class CommandBuilder:

    def __init__(self, customer: str, db_session):
        self._customer = customer
        self._db_session = db_session

        self._basket = {}  # mapping basket items

    def get_basket(self):
        return self._basket

    def add_article(self, article: Article, number: int):
        # check stocks
        if article.number - number < 0:
            raise NotEnoughArticle()

        self._basket[article.id] = BasketItem(article, number)

    def remove_article(self, article):
        if article.id in self._basket:
            del(self._basket[article.id])

    def update_number(self, article, number):
        if article not in self._basket:
            raise ResourceNotFound()
        basket_item = self._basket[article.id]
        if number > basket_item.article.number:
            # check stocks
            raise NotEnoughArticle()

        basket_item.number = number

    def get_price(self):
        price = 0
        for _, item in self._basket.items():
            price += item.article.price

        return price

    def register_command(self):
        command = Command(status='pending',
                          customer=self._customer)
        for _, item in self._basket.items():
            article = item.article
            command.add_article(article, item.number)
            # update article stocks
            article.stock = article.stock - item.number

        self._db_session.add(command)
        self._db_session.flush()

        return command.id


class BasketItem:
    article = None
    number = None

    def __init__(self, article, number):
        self.article = article
        self.number = number

    def to_dict(self):
        return {
            "article": self.article.to_dict(),
            "number": self.number
        }
