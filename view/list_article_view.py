from model.dao.article_dao import ArticleDAO
from view.view import View


class ListArticleView(View):

    def __init__(self, db_session):
        self._article_dao = ArticleDAO(db_session)

    def show(self):
        articles = self._article_dao.get_all()
        print("Article:")
        for article in articles:
            print("- %s: %s" % (article.name, article.description))
            print("     price: %d" % article.price)
            print("     items: %d" % article.number)
