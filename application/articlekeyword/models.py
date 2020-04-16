from application import db
from sqlalchemy.orm import relationship, backref
from application.models import Base
from application.artikkelit.models import Artikkeli
from application.keyword.models import Keyword

class ArticleKeyword(Base):

    __tablename__ = "articlekeyword"

    id = db.Column(db.Integer, primary_key = True)
    article_id = db.Column(db.Integer, db.ForeignKey('artikkeli.id'))
    keyword_id = db.Column(db.Integer, db.ForeignKey('keyword.id'))

    article = relationship(Artikkeli, backref=backref("articlekeyword", cascade="all, delete-orphan"))
    keyword = relationship(Keyword, backref=backref("articlekeyword", cascade="all, delete-orphan"))
