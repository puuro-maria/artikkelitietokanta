from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class ArtikkeliForm(FlaskForm):
    name = StringField("Title", [validators.DataRequired()])
    publisher = StringField("Publisher", [validators.DataRequired()])
    authors = StringField("Author", [validators.DataRequired()])
    source = StringField("Source", [validators.DataRequired()])
    year = IntegerField("Year published", [validators.DataRequired()])

    class Meta:
        csrf = False