import unittest
import uuid
from unittest.mock import MagicMock
from model.mapping.article import Article
from controller.article_controller import ArticleController
from exceptions import ResourceNotFound, Conflict


class TestArticleController(unittest.TestCase):
    """
    Unit Tests Article Controller
    https://docs.python.org/fr/3/library/unittest.html
    """

    def setUp(self) -> None:
        """
        Function called before each test
        """
        # Mock store (we do not want a database connexion)
        # https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
        self.store = MagicMock()
        self.article_controller = ArticleController(self.store)

    def test_create_article(self):
        # Mock store create function
        self.store.article().create = MagicMock()
        # article not exists
        self.store.article().get_by_name.side_effect = ResourceNotFound()

        self.article_controller.set_name("toto")
        self.article_controller.set_price(12.5)
        self.article_controller.set_description("test")
        self.article_controller.set_article_type("test")
        self.article_controller.set_number(2)
        article = self.article_controller.register()

        self.store.article().create.assert_called_once()

        self.assertEqual(article.name, "toto")
        self.assertEqual(article.price, 12.5)
        self.assertEqual(article.description, "test")
        self.assertEqual(article.article_type, "test")
        self.assertEqual(article.number, 2)

    def test_set_name_already_exists(self):
        # No resourceNotFound will be raised when search article
        with self.assertRaises(Conflict):
            self.article_controller.set_name("toto")

    def test_update_article(self):
        # Mock store create function
        self.store.article().update = MagicMock()
        # article not exists
        self.store.article().get_by_name.side_effect = ResourceNotFound()

        article = Article(
            id=str(uuid.uuid4()),
            name="test",
            price=3.5,
            number=10,
            description="Test test",
            article_type="test"
        )
        self.article_controller.from_article(article)
        self.assertEqual(self.article_controller.get_name(), "test")
        self.assertEqual(self.article_controller.get_price(), 3.5)
        self.assertEqual(self.article_controller.get_number(), 10)
        self.assertEqual(self.article_controller.get_description(), "Test test")
        self.assertEqual(self.article_controller.get_article_type(), "test")

        self.article_controller.register()
        self.store.article().update.assert_called_once()
