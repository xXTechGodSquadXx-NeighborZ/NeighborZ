from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, validators, ValidationError, SelectField


def reason_check(form, field):
    if field.data == "error":
        raise ValidationError('Please select a reason.')


class ContactForm(FlaskForm):
    name = StringField(
        "Name",  [validators.Required("Please enter your name.")])
    email = StringField("Email",  [validators.Required(
        "Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = StringField(
        "Subject",  [validators.Required("Please enter a subject.")])
    reason = SelectField(u'Reason for Contacting', [validators.Required("Please select a reason."), reason_check], choices=[
        ('error', 'Please select a reason for contacting'),
        ('Issue', 'Issue'),
        ('Suggestion', 'Suggestion'),
        ('Press', 'Press Inquiry'),
        ('Other', 'Other, please specify in text box below')])
    message = TextAreaField(
        "Message",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")
