
from model.mapping.user import User
from model.mapping.customer import Customer
from model.dao.user_dao import UserDAO
from exceptions import Error


class CustomerController(User):
    """
    customer actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_users(self):
        with self._database_engine.new_session() as session:
            users = UserDAO(session).get_all(type='customer')
            users_data = [user.to_dict() for user in users]
        return users_data

    def create_user(self, data):
        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save user in database
                customer = Customer(username=data['username'],
                                    firstname=data['firstname'],
                                    lastname=data['lastname'],
                                    email=data.get('email'))
                session.add(customer)
                user_data = customer.to_dict()
                return user_data
        except Error as e:
            # log error
            raise e
