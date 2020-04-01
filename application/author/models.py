from application import db
from sqlalchemy.orm import relationship
from application.models import Base

class Author(Base):

    __tablename__ = "author"

    name = db.Column(db.String(144), nullable=False)

    articles = relationship("Artikkeli", secondary="articleauthor")

    def __init__(self, name):
        self.name = name

