from vue.user.add import AddUserQt
from PySide6.QtWidgets import QWidget,  QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent
from vue.user.show import ListUserQt


class DeleteUserQt(QWidget):
    def __init__(self, member_controller, id):
        self._member_controller = member_controller
        super().__init__()
        self.user_id = id
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.email = QLineEdit()
        self.setup()
        self.fillform()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout
        self.first_name.setEnabled(False)
        Layout.addRow("First Name", self.first_name)
        self.last_name.setEnabled(False)
        Layout.addRow("Last Name", self.last_name)
        self.email.setEnabled(False)
        Layout.addRow("Email", self.email)
        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_delete = QPushButton('Delete User', self)
        btn_delete.clicked.connect(self.deleteUser)
        btn_delete.resize(btn_delete.sizeHint())
        btn_delete.move(90, 100)
        ValidationLayout.addWidget(btn_delete)

        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Quit', self)
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

    def deleteUser(self):
        # Show subscription formular
        self._member_controller.delete_member(self.user_id)
        self.close()


    def fillform(self):
        user = self._member_controller.get_member(self.user_id)
        self.first_name.setText(user['firstname'])
        self.last_name.setText(user['lastname'])
        self.email.setText(user['email'])