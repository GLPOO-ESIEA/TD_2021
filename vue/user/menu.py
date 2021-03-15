from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QVBoxLayout, QDialog
from PySide6.QtGui import QCloseEvent

#https://zetcode.com/gui/pysidetutorial/
#https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html
#https://doc.qt.io/qtforpython-6/contents.html


class UserQtView(QWidget):
    def __init__(self):
        super().__init__()

    def setup(self, name):
        #input nom
        #name_ipt = QLineEdit(name, self)
        #name_ipt.resize(name_ipt.sizeHint())
        #name_ipt.move(0, 40)
        #input Prenom
        #input email
        #selectbox Type


        # list user inmultiple select ? multiple line ?
        # Button edit search & delete
        # Button Add
        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('edit user')

        self.show()
    #def edit_user()
        # Edit/Add vue
        # hide userQtView 

    #def search_user()
        #  
        # hide userQtView 


    #def delete user():
        #
        # hide userQtView 


