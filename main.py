from model.database import DatabaseEngine
from model.store import Store
from exceptions import ResourceNotFound
from model import *

from view.main_view import MainView


def main():
    print("## Welcome to the Shop ##\n")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()

    # Database session is created when opening the app. All data will be commit in database at the end of the program.
    with database_engine.new_session() as db_session:
        # Init store object
        store = Store(db_session)

        # Feed admin
        try:
            store.user().get_by_username('admin')
        except ResourceNotFound:
            admin = Admin(username="admin", firstname="admin", lastname="admin", email="contact@shop.fr")
            db_session.add(admin)

        try:
            # Run main view
            MainView(store).show()
        except KeyboardInterrupt:
            pass
        print("See you soon ! Bye !")


if __name__ == "__main__":
    main()
