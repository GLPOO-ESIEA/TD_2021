from view.view import View
from model.mapping.user import User


class ShowProfileView(View):

    def __init__(self, user: User):
        self._user = user

    def show(self):
        print("profile: ")
        print(self._user.firstname.capitalize(), self._user.lastname.capitalize())
        print("email:", self._user.email)
        print("type:", self._user.user_type)
