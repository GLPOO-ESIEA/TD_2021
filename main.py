from model.database import DatabaseEngine
from model.store import Store
from model.mapping.admin import Admin
from model import *

from view.main_view import MainView


def main():
    print("## Welcome to the Shop ##\n")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()

    with database_engine.new_session() as db_session:
        # Feed admin
        admin = Admin(username="admin", firstname="admin", lastname="admin", email="contact@shop.fr")
        db_session.merge(admin)
        # Init store object
        store = Store(db_session)
        # Run main view
        MainView(store).show()


if __name__ == "__main__":
    main()
