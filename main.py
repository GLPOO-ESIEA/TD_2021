from model.database import DatabaseEngine
from model.dao.user_dao import UserDAO
from model import *

from view.main_view import MainView


def main():
    print("## Welcome to the Shop ##\n")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()

    with database_engine.new_session() as db_session:
        user_dao = UserDAO(db_session)
        MainView(user_dao).show()


if __name__ == "__main__":
    main()
