from model.mapping.customer import Customer
from sqlalchemy import inspect
from controller.command_builder import CommandBuilder
from controller.validation.user_validation import UserValidation


class CustomerController:

    def __init__(self, customer: Customer):
        self._customer = customer

    def create_command(self):
        return CommandBuilder(self._customer)

    def get_commands(self):
        return self._customer.commands

    def update_profile(self, **kwargs):
        for key in ['username', 'firstname', 'lastname', 'email']:
            if kwargs.get(key) is not None:  # Check key is in user_data
                setattr(self._customer, key, kwargs[key])  # update attribute key in user object
        UserValidation(self._customer).validate()
        return self

    def delete_account(self):
        db_session = inspect(self._customer).session
        db_session.delete(self._customer)
        self._customer = None
