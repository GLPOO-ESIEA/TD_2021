import sys

from PySide6.QtWidgets import QApplication
from vue.menu import MenuWindow

#https://realpython.com/python-pyqt-layout/

def run():
    app = QApplication(sys.argv)

    menu = MenuWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
