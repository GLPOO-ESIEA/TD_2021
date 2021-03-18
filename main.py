import sys

from controller.member_controller import MemberController
from model.database import DatabaseEngine
from PySide6.QtWidgets import QApplication
from vue.menu import MenuWindow

#https://realpython.com/python-pyqt-layout/
#https://www.learnpyqt.com/tutorials/creating-multiple-windows/


def run():
    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()
    admin_controller = MemberController(database_engine)
    app = QApplication(sys.argv)

    menu = MenuWindow(admin_controller)

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
