from PySide6.QtWidgets import QWidget,  QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent


class AddUserQt(QWidget):
    def __init__(self, member_controller):
        self._member_controller = member_controller
        super().__init__()
        ##
        first_name = ""
        last_name = ""
        email = ""
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout
        self.first_name = QLineEdit()
        Layout.addRow("First Name", self.first_name)
        self.last_name = QLineEdit()
        #last_name = QLineEdit()
        Layout.addRow("Last Name", self.last_name)
        self.email = QLineEdit()
        #email = QLineEdit()
        Layout.addRow("Email", self.email)
        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Add User', self)
        btn_add.clicked.connect(self.addUser)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(90, 100)
        ValidationLayout.addWidget(btn_add)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Quit', self)
        btn_cancel.clicked.connect(self.close)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit ?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def addUser(self):
        # Show subscription formular
        data = {'firstname': self.first_name.text(), 'lastname': self.last_name.text(), 'email': self.email.text(), 'type': 'customer'}
        print(data)
        self._member_controller.create_member(data)
        members = self._member_controller.list_members()

        print("Members: ")
        for member in members:
            print("* %s %s (%s) - %s" % (   member['firstname'].capitalize(),
                                            member['lastname'].capitalize(),
                                            member['email'],
                                            member['type']))