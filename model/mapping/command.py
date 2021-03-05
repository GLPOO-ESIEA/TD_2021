from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Command(Base):
    __tablename__ = 'command'

    id = Column(String(36), default=generate_id, primary_key=True)

    # Sport is unique in database
    date = Column(String(50), nullable=False, unique=True)
    status = Column(String(10), nullable=True)  # TODO: update with Enum
    customer_id = Column(String(36), ForeignKey("customer.id"), nullable=True)

    customer = relationship("Customer", cascade="all,delete-orphan", single_parent=True)
    articles = relationship("ArticleAssociation", back_populates="article")

    def __repr__(self):
        return "<Sport %s>" % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            'articles': [articleAsso.todict() for articleAsso in self.articles]
        }


class CommandAssociation(Base):
    """
    Association class between person and sport
    help relationship: https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
    """
    __tablename__ = 'command_associations'
    __table_args__ = (UniqueConstraint('command_id', 'article_id'),)

    command_id = Column(String(36), ForeignKey(Command.id), primary_key=True)
    article_id = Column(String(36), ForeignKey('article.id'), primary_key=True)
    number = Column(Integer, nullable=False)
    command = relationship("Command", back_populates="articles")
    article = relationship("Sport", back_populates="command")

    def todict(self):
        return {
            "number": self.number,
            "article": self.article.todict()
        }
