from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=20)])
    name = StringField("Name", [validators.Length(min=4, max=20)])
    password = PasswordField("Password", [validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
  
    class Meta:
        csrf = False