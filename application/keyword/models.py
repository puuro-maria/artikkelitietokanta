from application import db
from sqlalchemy.orm import relationship
from application.models import Base

class Keyword(Base):

    __tablename__ = "keyword"

    name = db.Column(db.String(144), nullable=False)

    articles = relationship("Artikkeli", secondary="articlekeyword")

    def __init__(self, name):
            self.name = name

