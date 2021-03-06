from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class ArtikkeliForm(FlaskForm):
    name = StringField("Title", [validators.DataRequired()])
    publisher = StringField("Publisher", [validators.DataRequired()])
    authors = StringField("Authors", [validators.DataRequired()])
    keywords = StringField("Keywords", [validators.DataRequired()])
    source = StringField("Source", [validators.DataRequired()])
    year = IntegerField("Year published", [validators.NumberRange(min=0, max=None, message="Positive integer required")])
    read = BooleanField("Read")

    class Meta:
        csrf = False