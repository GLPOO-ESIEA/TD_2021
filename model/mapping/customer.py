from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from model.mapping.user import User
from model.mapping import generate_id


class Customer(User):
    __tablename__ = 'customer'

    id = Column(String(36), ForeignKey(User.id), default=generate_id, primary_key=True)
    commands = relationship("Command",
                            backref=backref("customer", lazy='subquery'))

    __mapper_args__ = {
        'polymorphic_identity': 'member',
    }

    def __repr__(self):
        return "<Member(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        _dict = super().to_dict()
        return _dict
