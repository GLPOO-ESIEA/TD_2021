from model.mapping.article import Article
from model.store import Store


class ArticleController:
    """
    article actions
    """

    def __init__(self, store: Store):
        self._store = store

    def new_article(self, name: str, price: float, number: int, description="", article_type=""):
        # Save article in database
        article = Article(name=name,
                          price=price,
                          number=number,
                          description=description,
                          article_type=article_type)
        self._store.article().create(article)
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
        self._store.article().update(article)
        return article

    def delete_article(self, article):
        self._store.article().delete(article)
