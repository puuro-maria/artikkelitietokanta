from application import db
from sqlalchemy.orm import relationship
from application.models import Base

class Artikkeli(Base):

    name = db.Column(db.String(144), nullable=False)
    publisher = db.Column(db.String(144), nullable=False)
    source = db.Column(db.String(144), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    authors = relationship("Author", secondary="articleauthor")

    def __init__(self, name, authors, publisher, source, year):
        self.name = name
        self.authors = authors
        self.publisher = publisher
        self.source = source
        self.year = year
