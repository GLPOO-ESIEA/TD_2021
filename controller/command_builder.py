from model.mapping.article import Article
from model.mapping.customer import Customer
from model.mapping.command import Command
from model.mapping.command_status_enum import CommandStatusEnum
from model.store import Store
from exceptions import NotEnoughArticle, ResourceNotFound


class CommandBuilder:
    """
    Build command for a customer
    Design pattern builder (function register must be call at end)
    """

    def __init__(self, customer: Customer, store: Store):
        self._customer = customer
        self._store = store
        self._basket = {}  # mapping basket items

    def get_basket(self):
        return [self._basket[item] for item in self._basket]

    def add_article(self, article: Article, number: int):
        # check stocks
        if article.number - number < 0:
            raise NotEnoughArticle()

        self._basket[article.id] = BasketItem(article, number)

    def remove_article(self, article: Article):
        if article.id in self._basket:
            del(self._basket[article.id])

    def update_number(self, article: Article, number: int):
        if article.id not in self._basket:
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

    def register(self):
        command = Command(status=CommandStatusEnum.PENDING,
                          customer=self._customer)
        for _, item in self._basket.items():
            article = item.article
            command.add_article(article, item.number)
            # update article stocks
            article.number = article.number - item.number

        self._store.command().create(command)

        return command.id


class BasketItem:
    article = None
    number = None

    def __init__(self, article: Article, number: int):
        self.article = article
        self.number = number
