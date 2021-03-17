from vue.window import BasicWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent
from vue.user.show import ListUserQt
from controller.member_controller import MemberController


class MenuWindow(BasicWindow):
    def __init__(self, member_controller):
        self._member_controller = member_controller
        super().__init__()
        self.listUserWindow = None

        self.setup()

    def setup(self):
        btn_list = QPushButton('List user', self)
        btn_list.resize(btn_list.sizeHint())
        btn_list.move(0, 0)
        btn_list.clicked.connect(self.list_user)
        #btn_add_user = QPushButton('add user', self)
        #btn_add_user.resize(btn_add_user.sizeHint())
        #btn_add_user.move(0, 20)
        #btn_add_user.clicked.connect(self.add_user)

        #btn_edit_user = QPushButton('edit user', self)
        #btn_edit_user.resize(btn_edit_user.sizeHint())
        #btn_edit_user.move(0, 40)
        #btn_search_user = QPushButton('search user', self)
        #btn_search_user.resize(btn_edit_user.sizeHint())
        #btn_search_user.move(0, 60)

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        layout = QVBoxLayout()
        layout.addWidget(btn_list)
        #layout.addWidget(btn_add_user)
        #layout.addWidget(btn_edit_user)
        #layout.addWidget(btn_search_user)
        layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Shop application Menu')
        self.setLayout(layout)
        self.show()

    #def add_user(self):
    #    if self.addUserWindow is None:
    #        self.addUserWindow = AddUserQt(self._member_controller)
    #    self.addUserWindow.show()
    def list_user(self):
        if self.listUserWindow is None:
           self.listUserWindow = ListUserQt(self._member_controller)
        self.listUserWindow.show()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit ?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()