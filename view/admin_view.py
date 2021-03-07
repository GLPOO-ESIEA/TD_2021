from view.view import View


class AdminView(View):
    """
    Admin View
    Admin specific interfaces
    """

    def __init__(self, admin_controller):
        self._admin_controller = admin_controller

    def show(self):
        pass
