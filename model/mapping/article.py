from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint, Float, Integer


class Article(Base):
    __tablename__ = 'article'
    __table_args__ = (UniqueConstraint('name'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(256), nullable=False)
    type = Column(String(10), nullable=False)
    number = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Article %s (%s)>" % (self.name, self.type)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.type,
            "price": self.price,
            "remain": self.number
        }
