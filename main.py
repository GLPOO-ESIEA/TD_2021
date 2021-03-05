
from model.database import DatabaseEngine
from model import *


def main():
    print("Welcome to the Shop")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()
    # admin_controller = MemberController(database_engine)
    # AdminVue(admin_controller).admin_shell()


if __name__ == "__main__":
    main()
