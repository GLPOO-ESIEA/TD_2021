from model.mapping.article import Article
from model.dao.article_dao import ArticleDAO


class ArticleController:
    """
    article actions
    """

    def __init__(self, article_dao: ArticleDAO):
        self._article_dao = article_dao

    def new_article(self, name: str, price: float, number: int, description="", article_type=""):
        # Save article in database
        article = Article(name=name,
                          price=price,
                          number=number,
                          description=description,
                          article_type=article_type)
        self._article_dao.create(article)
        return article

    def update_article(self, article, name=None, price=None, description=None, number=None):
        if name is not None:
            article.name = name
        if price is not None:
            article.price = price
        if description is not None:
            article.description = description
        if number is not None:
            article.number = number
        self._article_dao.update(article)
        return article

    def delete_article(self, article):
        self._article_dao.delete(article)
