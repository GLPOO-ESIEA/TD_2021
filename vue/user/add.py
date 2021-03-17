from PySide6.QtWidgets import QWidget,  QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox, QComboBox
from PySide6.QtGui import QCloseEvent
from vue.common import Common
from vue.user.show import ListUserQt


class AddUserQt(QWidget):
    def __init__(self, member_controller):
        self._member_controller = member_controller
        super().__init__()
        ##
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.email = QLineEdit()
        self.type = QComboBox()


        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("First Name", self.first_name)

        Layout.addRow("Last Name", self.last_name)

        Layout.addRow("Email", self.email)

        self.type.addItem("customer")
        self.type.addItem("seller")
        Layout.addRow("Account type", self.type)
        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Add User', self)
        btn_add.clicked.connect(self.addUser)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(90, 100)
        ValidationLayout.addWidget(btn_add)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Close', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def quitEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit ?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()

    def addUser(self):
        # Show subscription formular
        data = {'firstname': self.first_name.text(),
                'lastname': self.last_name.text(),
                'email': self.email.text(),
                'type': self.type.currentText()}
        print(data)
        self._member_controller.create_member(data)

        members = self._member_controller.list_members()

        print("Members: ")
        for member in members:
            print("* %s %s (%s) - %s" % (   member['firstname'].capitalize(),
                                            member['lastname'].capitalize(),
                                            member['email'],
                                            member['type']))
        self.close()