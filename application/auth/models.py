from application import db
from application.models import Base

from sqlalchemy.orm import relationship
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    isadmin = db.Column(db.Boolean, nullable=False)

    artikkelit = db.relationship("Artikkeli", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.isadmin=0
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(self):
        if self.isadmin:
            return ["ADMIN", "USER"]
        else: 
            return ["USER"]

    @staticmethod
    def account_summary(account_id):
        stmt = text("SELECT username, account.name, COUNT(artikkeli.id) AS 'articles', SUM(artikkeli.read) AS 'read articles'"
                    "FROM account INNER JOIN artikkeli ON account.id = artikkeli.account_id "
                    "WHERE account.id = :account_id").params(account_id = account_id)
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"username":row[0], "name":row[1], "articles":row[2], "unread":row[3]})
        
        return response
