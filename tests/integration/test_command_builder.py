import unittest
from model.database import DatabaseEngine
from model.store import Store
from model.mapping.customer import Customer
from model.mapping.article import Article
from model.mapping.command_status_enum import CommandStatusEnum
from controller.command_builder import CommandBuilder
from exceptions import NotEnoughArticle, InvalidData


class TestCommandBuilder(unittest.TestCase):
    """
    Integration Tests Command Builder
    https://docs.python.org/fr/3/library/unittest.html
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        Function called before the first test
        """
        cls._database_engine = DatabaseEngine()  # User memory sqlite
        cls._database_engine.create_database()
        with cls._database_engine.new_session() as session:
            # feed customer
            customer = Customer(username="user",
                                firstname="test",
                                lastname="test",
                                email="test@test.fr")
            session.add(customer)
            # feed articles
            article_1 = Article(name="test_article", price=3.5,
                                description="Test article", number=5,
                                article_type="test")
            article_2 = Article(name="article_2", price=10,
                                description="Test article", number=5,
                                article_type="test")
            session.add(article_1)
            session.add(article_2)
            session.flush()
            cls.customer_id = customer.id
            cls.article_1_id = article_1.id
            cls.article_2_id = article_2.id

    def setUp(self) -> None:
        """
        Function called before each test
        """
        self.db_session = self._database_engine.new_session()
        self.store = Store(self.db_session)
        self.customer = self.store.user().get(self.customer_id)
        self.article_1 = self.store.article().get(self.article_1_id)
        self.article_2 = self.store.article().get(self.article_2_id)
        self.command_builder = CommandBuilder(self.customer, self.store)

    def tearDown(self) -> None:
        """
        Function called after each test
        """
        self.db_session.close()

    def test_add_article(self):
        self.command_builder.add_article(self.article_1, 2)

    def test_add_article_not_enough_items(self):
        with self.assertRaises(NotEnoughArticle):
            self.command_builder.add_article(self.article_1, 6)

    def test_add_article_already_in_basket(self):
        self.command_builder.add_article(self.article_1, 2)
        self.command_builder.add_article(self.article_1, 3)
        basket = self.command_builder.get_basket()
        self.assertEqual(len(basket), 1)
        self.assertEqual(basket[0].article, self.article_1)
        self.assertEqual(basket[0].number, 3)

    def test_get_basket(self):
        # empty
        self.assertEqual(len(self.command_builder.get_basket()), 0)
        # add article
        self.command_builder.add_article(self.article_1, 2)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 1)

    def test_remove_article(self):
        # add article
        self.command_builder.add_article(self.article_1, 1)
        self.command_builder.add_article(self.article_2, 3)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 2)
        # del article
        self.command_builder.remove_article(self.article_1)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 1)

    def test_remove_article_not_found(self):
        self.command_builder.add_article(self.article_1, 1)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 1)
        # del article (Not added)
        self.command_builder.remove_article(self.article_2)
        # get
        self.assertEqual(len(self.command_builder.get_basket()), 1)

    def test_get_price(self):
        self.command_builder.add_article(self.article_1, 1)
        self.command_builder.add_article(self.article_2, 2)
        self.assertEqual(self.command_builder.get_price(), 23.5)

    def test_register(self):
        # prepare command
        article = self.store.article().get(self.article_1_id)
        article_2 = self.store.article().get(self.article_2_id)
        self.command_builder.add_article(article, 1)
        self.command_builder.add_article(article_2, 2)

        # check data send to store
        command = self.command_builder.register()

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
