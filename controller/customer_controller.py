from model.mapping.customer import Customer
from sqlalchemy import inspect
from controller.command_builder import CommandBuilder
from controller.validation.user_validation import UserValidation
from model.dao.customer_dao import CustomerDAO


class CustomerController:

    def __init__(self, customer: Customer):
        self._customer = customer
        db_session = inspect(self._customer).session
        self._customer_dao = CustomerDAO(db_session)

    def create_command(self):
        return CommandBuilder(self._customer)

    def get_commands(self):
        return self._customer.commands

    def update_profile(self, **kwargs):
        for key in ['username', 'firstname', 'lastname', 'email']:
            if kwargs.get(key) is not None:  # Check key is in user_data
                setattr(self._customer, key, kwargs[key])  # update attribute key in user object
        UserValidation(self._customer).validate()
        self._customer_dao.update(self._customer)
        return self

    def delete_account(self):
        self._customer_dao.delete(self._customer)
        self._customer = None
