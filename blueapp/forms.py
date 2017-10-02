from flask_wtf import Form
from wtforms.fields.html5 import EmailField
from wtforms import StringField, TextAreaField, validators

class MailingListForm(Form):
    email = EmailField('Email Address',
                       [validators.DataRequired(),
                        validators.Email()])

class SendMailForm(Form):
    title = StringField('Title', [validators.Length(min=1)])
    content = TextAreaField('Content', [validators.InputRequired()])
