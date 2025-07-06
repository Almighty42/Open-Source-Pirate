from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

def validate_password(field):
    if field.data != 'pass123':
        raise ValidationError('Password is incorrect.')

class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), lambda form, field: validate_password(field)])
    submit = SubmitField('Sign in')

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=6)])
    pub_date = StringField('Publish date')
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=50)])
    submit = SubmitField('Publish')
