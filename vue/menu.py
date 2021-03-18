from vue.window import BasicWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton
from vue.user.show import ListUserQt
from controller.member_controller import MemberController


class MenuWindow(BasicWindow):

    def __init__(self, member_controller: MemberController):
        self._member_controller = member_controller
        super().__init__()
        self.listUserWindow = None

        self.setup()

    def setup(self):
        btn_list = QPushButton('List user', self)
        btn_list.resize(btn_list.sizeHint())
        btn_list.move(0, 0)
        btn_list.clicked.connect(self.list_user)

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        layout = QVBoxLayout()
        layout.addWidget(btn_list)
        layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Shop application Menu')
        self.setLayout(layout)
        self.show()

    def list_user(self):
        if self.listUserWindow is None:
            self.listUserWindow = ListUserQt(self._member_controller)
        self.listUserWindow.show()
