from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = TextField('Name')
    email = TextField('Email')
    message = TextAreaField('Message')
    submit = SubmitField('SEND')

