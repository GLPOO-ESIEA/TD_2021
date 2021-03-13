import unittest
from unittest.mock import MagicMock
import uuid
from model.mapping.customer import Customer
from model.mapping.article import Article
from model.mapping.command_status_enum import CommandStatusEnum
from controller.command_builder import CommandBuilder
from exceptions import NotEnoughArticle, InvalidData


class TestCommandBuilder(unittest.TestCase):
    """
    Unit Tests Command Builder
    https://docs.python.org/fr/3/library/unittest.html
    """

    def setUp(self) -> None:
        """
        Function called before each test
        """
        self.customer = Customer(id=str(uuid.uuid4()), username="user", firstname="test", lastname="test",
                                 email="test@test.fr")
        # Mock store (we do not want a database connexion)
        # https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
        self.store = MagicMock()
        self.command_builder = CommandBuilder(self.customer, self.store)

    def test_add_article(self):
        article = Article(name="test_article", description="Test article", number=5)
        self.command_builder.add_article(article, 2)

    def test_add_article_not_enough_items(self):
        article = Article(name="test_article", description="Test article", number=5)
        with self.assertRaises(NotEnoughArticle):
            self.command_builder.add_article(article, 6)

    def test_add_article_already_in_basket(self):
        article = Article(name="test_article", description="Test article", number=5)
        self.command_builder.add_article(article, 2)
        self.command_builder.add_article(article, 3)
        basket = self.command_builder.get_basket()
        self.assertEqual(len(basket), 1)
        self.assertEqual(basket[0].article, article)
        self.assertEqual(basket[0].number, 3)

    def test_get_basket(self):
        # empty
        self.assertEqual(len(self.command_builder.get_basket()), 0)
        # add article
        article = Article(id=str(uuid.uuid4()), name="test_article", description="Test article", number=5)
        self.command_builder.add_article(article, 2)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 1)
        article = Article(name="test_article", description="Test article", number=5)
        self.command_builder.add_article(article, 2)

    def test_remove_article(self):
        # add article
        article = Article(id=str(uuid.uuid4()), name="article_1", description="Test article", number=5)
        article_2 = Article(id=str(uuid.uuid4()), name="article_2", description="Test article", number=5)
        self.command_builder.add_article(article, 1)
        self.command_builder.add_article(article_2, 3)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 2)
        # del article
        self.command_builder.remove_article(article)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 1)

    def test_remove_article_not_found(self):
        article = Article(id=str(uuid.uuid4()), name="article_1", description="Test article", number=5)
        article_2 = Article(id=str(uuid.uuid4()), name="article_2", description="Test article", number=5)
        self.command_builder.add_article(article, 1)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 1)
        # del article (Not added)
        self.command_builder.remove_article(article_2)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 1)

    def test_get_price(self):
        article = Article(id=str(uuid.uuid4()), name="article_1", price=3.5,
                          description="Test article", number=5)
        article_2 = Article(id=str(uuid.uuid4()), name="article_2", price=10,
                            description="Test article", number=5)
        self.command_builder.add_article(article, 1)
        self.command_builder.add_article(article_2, 2)
        self.assertEqual(self.command_builder.get_price(), 23.5)

    def test_register(self):
        # prepare command
        article = Article(id=str(uuid.uuid4()), name="article_1", price=3.5,
                          description="Test article", number=5)
        article_2 = Article(id=str(uuid.uuid4()), name="article_2", price=10,
                            description="Test article", number=5)
        self.command_builder.add_article(article, 1)
        self.command_builder.add_article(article_2, 2)

        # Mock store create function
        self.store.command().create = MagicMock()

        # check data send to store
        self.command_builder.register()
        self.store.command().create.assert_called_once()
        command = self.store.command().create.call_args_list[0][0][0]
        self.assertEqual(command.status, CommandStatusEnum.PENDING)
        self.assertEqual(command.customer, self.customer)
        self.assertEqual(len(command.articles), 2)
        for item in command.articles:
            self.assertIn(item.article, [article, article_2])
            if item.article == article:
                self.assertEqual(item.number, 1)
            elif item.article == article_2:
                self.assertEqual(item.number, 2)

        # check number items updated
        self.assertEqual(article.number, 4)
        self.assertEqual(article_2.number, 3)

    def test_register_empty_basket(self):
        with self.assertRaises(InvalidData):
            # check data send to store
            self.command_builder.register()


if __name__ == '__main__':
    unittest.main()
