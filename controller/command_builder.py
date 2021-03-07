from model.dao.article_dao import ArticleDAO
from exceptions import NotEnoughArticle, ResourceNotFound
from model.mapping.command import Command


class CommandBuilder:

    def __init__(self, customer_id: str, database_engine):
        self._customer_id = customer_id
        self._database_engine = database_engine

        self._basket = {}  # mapping basket items

    def get_basket(self):
        return [item.to_dict() for _, item in self._basket]

    def add_article(self, article_id: str, number: int):
        with self._database_engine.new_session() as session:
            # get article
            article = ArticleDAO(session).get(article_id)
            # check stocks
            if article.number - number < 0:
                raise NotEnoughArticle()

            session.expunge(article)
            self._basket[article_id] = BasketItem(article, number)

    def remove_article(self, article_id):
        if article_id in self._basket:
            del(self._basket[article_id])

    def update_number(self, article_id, number):
        if article_id not in self._basket:
            raise ResourceNotFound()
        basket_item = self._basket[article_id]
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
        with self._database_engine.new_session() as session:
            command = Command(status='pending',
                              customer_id=self._customer_id)
            for _, item in self._basket.items():
                article = item.article
                session.merge(article)  # article was not bind to the session !
                command.add_article(article, item.number)
                # update article stocks
                article.stock = article.stock - item.number

            session.add(command)
            session.flush()

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
