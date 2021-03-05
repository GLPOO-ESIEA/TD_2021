from model.dao.dao_error_handler import dao_error_handler

from sqlalchemy import or_
from model.mapping.article import Article
from model.dao.dao import DAO


class ArticleDAO(DAO):
    """
    User Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    @dao_error_handler
    def get(self, id):
        return self._database_session.query(Article).filter_by(id=id).one()

    @dao_error_handler
    def get_all(self):
        return self._database_session.query(Article).order_by(Article.name).all()

    @dao_error_handler
    def search(self, string: str):
        return self._database_session.query(Article)\
            .filter(or_(Article.c.name.ilike("{}%".format(string)),
                        Article.c.description.ilike("{}%".format(string))))\
            .order_by(Article.name).all()
