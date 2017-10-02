from flask_wtf import Form
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

class MailingListForm(Form):
    email = EmailField('Email Address', [DataRequired(), Email()])
