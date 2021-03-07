
from model.database import DatabaseEngine
from model.dao.user_dao import UserDAO
from model import *

from vue.main_vue import MainVue


def main():
    print("## Welcome to the Shop ##\n")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()

    with database_engine.new_session() as db_session:
        user_dao = UserDAO(db_session)
        MainVue(user_dao).main()
    # admin_controller = MemberController(database_engine)
    # AdminVue(admin_controller).admin_shell()


if __name__ == "__main__":
    main()
