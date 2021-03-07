from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (UniqueConstraint('username'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)

    email = Column(String(256), nullable=False)

    user_type = Column(String(50), nullable=False)

    # https://docs.sqlalchemy.org/en/13/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': user_type
    }

    def __repr__(self):
        return "<user(%s %s %s)>" % (self.firstname, self.lastname.upper(), self.user_type)

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "type": self.user_type
        }
