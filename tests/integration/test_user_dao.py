import unittest
import uuid
from model.database import DatabaseEngine
from model.mapping.customer import Customer
from model.dao.user_dao import UserDAO
from exceptions import ResourceNotFound


class TestUserDAO(unittest.TestCase):
    """
    Integration Tests user DAO
    https://docs.python.org/fr/3/library/unittest.html
    """

    def setUp(self) -> None:
        """
        Function called before the first test
        """
        self.database_engine = DatabaseEngine()  # sqlite in memory
        self.database_engine.create_database()
        with self.database_engine.new_session() as session:
            # feed customer
            customer = Customer(username="user1",
                                firstname="John",
                                lastname="Do",
                                email="test@test.fr")
            session.add(customer)
            customer_2 = Customer(username="rstark",
                                  firstname="Rob",
                                  lastname="Stark",
                                  email="toto@test.fr")
            session.add(customer_2)
            session.flush()
            self.customer_1_id = customer.id
            self.customer_2_id = customer_2.id

    def tearDown(self) -> None:
        self.database_engine.remove_database()

    def test_get_user(self):
        with self.database_engine.new_session() as session:
            user_dao = UserDAO(session)
            customer = user_dao.get(self.customer_1_id)
            self.assertEqual(customer.username, "user1")

    def test_get_user_not_found(self):
        with self.database_engine.new_session() as session:
            user_dao = UserDAO(session)
            with self.assertRaises(ResourceNotFound):
                user_dao.get(str(uuid.uuid4()))

    def test_get_user_by_username(self):
        with self.database_engine.new_session() as session:
            user_dao = UserDAO(session)
            customer = user_dao.get_by_username("user1")
            self.assertEqual(customer.id, self.customer_1_id)

    def test_get_user_by_username_not_found(self):
        with self.database_engine.new_session() as session:
            user_dao = UserDAO(session)
            with self.assertRaises(ResourceNotFound):
                user_dao.get_by_username("user_not_found")

    def test_list_users(self):
        with self.database_engine.new_session() as session:
            user_dao = UserDAO(session)
            customers = user_dao.get_all()
            self.assertEqual(len(customers), 2)
            self.assertEqual(customers[0].username, "user1")
            self.assertEqual(customers[1].username, "rstark")

    def test_get_user_by_name(self):
        with self.database_engine.new_session() as session:
            user_dao = UserDAO(session)
            customer = user_dao.get_by_name(firstname="john", lastname="do")
            self.assertEqual(customer.id, self.customer_1_id)

    def test_get_user_by_name_not_found(self):
        with self.database_engine.new_session() as session:
            user_dao = UserDAO(session)
            with self.assertRaises(ResourceNotFound):
                user_dao.get_by_name(firstname="john", lastname="notfound")