from model.mapping.article import Article
from model.dao.article_dao import ArticleDAO


class ArticleController:
    """
    article actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_articles(self):
        with self._database_engine.new_session() as session:
            articles = ArticleDAO(session).get_all()
            articles_data = [article.to_dict() for article in articles]
        return articles_data

    def get_article(self, article_id):
        with self._database_engine.new_session() as session:
            article = ArticleDAO(session).get(article_id)
            article_data = article.to_dict()
        return article_data

    def new_article(self, name: str, price: float, number: int, description="", article_type=""):
        with self._database_engine.new_session() as session:
            # Save article in database
            article = Article(name=name,
                              price=price,
                              number=number,
                              description=description,
                              article_type=article_type)
            session.add(article)
            article_data = article.to_dict()
            return article_data

    def update_article(self, article_id, name=None, price=None, description=None, number=None):

        with self._database_engine.new_session() as session:
            article_dao = ArticleDAO(session)
            article = article_dao.get(article_id)
            if name is not None:
                article.name = name
            if price is not None:
                article.price = price
            if description is not None:
                article.description = description
            if number is not None:
                article.number = number
            article.flush()
            return article.to_dict()

    def delete_article(self, article_id):
        with self._database_engine.new_session() as session:
            article_dao = ArticleDAO(session)
            article = article_dao.get(article_id)
            session.delete(article)

    def search_article(self, string: str):

        # Query database
        with self._database_engine.new_session() as session:
            article_dao = ArticleDAO(session)
            articles = article_dao.search(string)
            return [article.to_dict() for article in articles]
