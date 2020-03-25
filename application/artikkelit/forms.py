from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class ArtikkeliForm(FlaskForm):
    name = StringField("Title")
    publisher = StringField("Publisher")
    source = StringField("Source")
    year = IntegerField("Year published")

    class Meta:
        csrf = False