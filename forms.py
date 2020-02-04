from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, validators, ValidationError


class ContactForm(FlaskForm):
    name = StringField(
        "Name",  [validators.Required("Please enter your name.")])
    email = StringField("Email",  [validators.Required(
        "Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = StringField(
        "Subject",  [validators.Required("Please enter a subject.")])
    message = TextAreaField(
        "Message",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")
