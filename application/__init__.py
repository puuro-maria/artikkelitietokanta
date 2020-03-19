
from flask import Flask
app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///artikkelit.db"

app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views
from application.artikkelit import models
from application.artikkelit import views


db.create_all()