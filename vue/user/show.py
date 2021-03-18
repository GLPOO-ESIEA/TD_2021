from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout
from vue.user.add import AddUserQt
from vue.user.edit import EditUserQt
from vue.user.delete import DeleteUserQt
from vue.user.search import SearchUserQt
from vue.window import BasicWindow
from controller.member_controller import MemberController


class ListUserQt(BasicWindow):
    def __init__(self, member_controller: MemberController):
        self._member_controller = member_controller
        super().__init__()
        self.addUserWindow = None
        self.editUserWindow = None
        self.deleteUserWindow = None
        self.searchUserWindow = None
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()

        self.btn_add_user = QPushButton('Add user', self)
        self.btn_edit_user = QPushButton('Edit user', self)
        self.btn_delete_user = QPushButton('Delete user', self)
        self.btn_search_user = QPushButton('Search user', self)

        self.members = ""
        self.getmembers()

        self.list()
        self.side_menu()
        self.setLayout(self.layout)

    def getmembers(self):
        self.members = self._member_controller.list_members()

    def list(self):

        self.listwidget.clear()
        index = 0
        for member in self.members:
            self.listwidget.insertItem(index, "* %s %s (%s) - %s" % (
                member['firstname'],
                member['lastname'],
                member['email'],
                member['type']))
            index += 1

        self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)

    def side_menu(self):

        self.btn_add_user.resize(self.btn_add_user.sizeHint())
        self.btn_add_user.move(60, 20)
        self.btn_add_user.clicked.connect(self.add_user)

        self.btn_edit_user.resize(self.btn_edit_user.sizeHint())
        self.btn_edit_user.move(60, 40)
        self.btn_edit_user.setEnabled(False)
        self.btn_edit_user.clicked.connect(self.edit_user)

        self.btn_delete_user.resize(self.btn_delete_user.sizeHint())
        self.btn_delete_user.move(60, 60)
        self.btn_delete_user.setEnabled(False)
        self.btn_delete_user.clicked.connect(self.delete_user)

        self.btn_search_user.resize(self.btn_edit_user.sizeHint())
        self.btn_search_user.move(60, 80)
        self.btn_search_user.clicked.connect(self.search_user)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_add_user)
        buttonlayout.addWidget(self.btn_edit_user)
        buttonlayout.addWidget(self.btn_delete_user)
        buttonlayout.addWidget(self.btn_search_user)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('User menu')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_edit_user.setEnabled(True)
        self.btn_delete_user.setEnabled(True)
        print(item.text())

    def refresh(self):
        self.getmembers()

        self.list()
        self.show()

    def add_user(self):
        if self.addUserWindow is None:
            self.addUserWindow = AddUserQt(self._member_controller, self)
        self.addUserWindow.show()

    def edit_user(self):
        if self.editUserWindow is None:
            user_id = self.get_user_id(self.listwidget.currentItem().text())
            self.editUserWindow = EditUserQt(self._member_controller, user_id, self)
        self.editUserWindow.show()

    def delete_user(self):
        if self.deleteUserWindow is None:
            user_id = self.get_user_id(self.listwidget.currentItem().text())
            self.deleteUserWindow = DeleteUserQt(self._member_controller, user_id, self)
        self.deleteUserWindow.show()

    def search_user(self):
        if self.searchUserWindow is None:
            self.searchUserWindow = SearchUserQt(self._member_controller, self)
        self.searchUserWindow.show()

    def get_user_id(self, userfromlist:str):
        for member in self.members:
            if "* " + member['firstname'] + " " + member['lastname'] + " (" + member['email'] + ") - " + member['type'] == userfromlist:
                print(member['id'])
                return member['id']
