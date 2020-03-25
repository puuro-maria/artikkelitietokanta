from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class ArtikkeliForm(FlaskForm):
    name = StringField("Title", [validators.Length(min=2)])
    publisher = StringField("Publisher", [validators.Length(min=2)])
    source = StringField("Source", [validators.Length(min=2)])
    year = IntegerField("Year published", [validators.Length(min=2)])

    class Meta:
        csrf = False