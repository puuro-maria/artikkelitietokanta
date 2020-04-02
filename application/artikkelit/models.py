from application import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from application.models import Base

class Artikkeli(Base):

    name = db.Column(db.String(144), nullable=False)
    publisher = db.Column(db.String(144), nullable=False)
    source = db.Column(db.String(144), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    authors = relationship("Author", secondary="articleauthor")

    def __init__(self, name, authors, publisher, source, year, read = False):
        self.name = name
        self.authors = authors
        self.publisher = publisher
        self.source = source
        self.year = year
        self.read = read

    @staticmethod
    def list_unread_articles(account_id=1):
        
        stmt = text("SELECT id, name, read, account_id FROM artikkeli WHERE (read = 0 OR read IS NULL) AND (account_id = :account_id)").params(account_id = account_id)
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id":row[0], "name": row[1], "read":row[2], "account_id": row[3]})

        return response
