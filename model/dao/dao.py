
class DAO:
    """
    DAO Interface Object
    """

    def __init__(self, database_session):
        self._database_session = database_session

    def get(self, id):
        raise NotImplementedError()

    def get_all(self):
        raise NotImplementedError()

    def create(self, entity):
        # https://docs.sqlalchemy.org/en/14/orm/session_transaction.html#session-subtransactions-migrating
        with self._database_session.begin_nested():
            self._database_session.add(entity)
            self._database_session.flush()

    def update(self, entity):
        with self._database_session.begin_nested():
            self._database_session.merge(entity)
            self._database_session.flush()

    def delete(self, entity):
        with self._database_session.begin_nested():
            self._database_session.delete(entity)
