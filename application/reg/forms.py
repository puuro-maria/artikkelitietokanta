from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    name = StringField("Name", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    confirm = PasswordField("Repeat Password", [validators.DataRequired()])
  
    class Meta:
        csrf = False