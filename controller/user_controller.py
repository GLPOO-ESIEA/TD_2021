from model.mapping.user import User
from model.store import Store
from model.mapping.command_status_enum import CommandStatusEnum
from exceptions import ResourceNotFound, Conflict
from controller.validation.validate import Validate


class UserController:

    def __init__(self, store: Store):
        self._store = store
        self._id = None
        self._username = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._user_type = None

    def from_user(self, user: User):
        self._id = user.id
        self._username = user.username
        self._firstname = user.firstname
        self._lastname = user.lastname
        self._email = user.email
        self._user_type = user.user_type

    def set_username(self, username):
        if username == self._username:
            return
        Validate().validate_name(username)
        try:
            self._store.user().get_by_username(username)
        except ResourceNotFound:
            self._username = username
        else:
            raise Conflict("User %s already exists" % username)

    def get_username(self):
        return self._username

    def set_firstname(self, firstname):
        Validate().validate_name(firstname)
        self._firstname = firstname

    def get_firstname(self):
        return self._firstname

    def set_lastname(self, lastname):
        Validate().validate_name(lastname)
        self._lastname = lastname

    def get_lastname(self):
        return self._lastname

    def set_email(self, email):
        Validate().validate_email(email)
        self._email = email

    def get_email(self):
        return self._email

    def get_user_type(self):
        return self._user_type

    def register(self):
        user = User(id=self._id,
                    username=self._username,
                    firstname=self._firstname,
                    lastname=self._lastname,
                    email=self._email,
                    user_type=self._user_type)
        if self._id is None:
            self._store.user().create(user)
            self._id = user.id
        else:
            self._store.user().update(user)
        return user

    def delete(self):
        if self._id is None:
            raise ResourceNotFound("User not registered")
        user = self._store.user().get(self._id)
        for command in user.commands:
            if command.status == CommandStatusEnum.PENDING:
                raise Conflict("Cannot remove user with pending commands")
        self._store.user().delete(user)
