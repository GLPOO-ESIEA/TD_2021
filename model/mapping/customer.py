from sqlalchemy import Column, String, ForeignKey
from model.mapping.user import User
from model.mapping import generate_id


class Customer(User):
    __tablename__ = 'customer'

    id = Column(String(36), ForeignKey(User.id), default=generate_id, primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

    def __repr__(self):
        return "<Member(%s %s)>" % (self.firstname, self.lastname.upper())
