from application import db
from sqlalchemy.orm import relationship, backref
from application.models import Base
from application.artikkelit.models import Artikkeli
from application.author.models import Author

class ArticleAuthor(Base):

    __tablename__ = "articleauthor"

    id = db.Column(db.Integer, primary_key = True)
    article_id = db.Column(db.Integer, db.ForeignKey('artikkeli.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    article = relationship(Artikkeli, backref=backref("articleauthor", cascade="all, delete-orphan"))
    author = relationship(Author, backref=backref("articleauthor", cascade="all, delete-orphan"))
