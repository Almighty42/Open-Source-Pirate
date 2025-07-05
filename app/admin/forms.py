from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

def validate_password(field):
    if field.data != 'pass123':
        raise ValidationError('Password is incorrect.')

class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), lambda form, field: validate_password(field)])
    submit = SubmitField('Sign in')

