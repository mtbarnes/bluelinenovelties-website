import os
from flask import Flask
from flask_script import Manager
from flask_admin import Admin
from flask_sslify import SSLify
from flask_basicauth import BasicAuth
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail

working_dir = os.path.dirname(os.path.realpath(__file__))
#template_dir = os.path.join(working_dir, 'templates')


app = Flask(__name__)
application = app
sslify = SSLify(app)

app.config.from_envvar('FLASK_CONFIG')
app.config['SECRET_KEY'] = '60e14db8cbc92633350de1395a54544f5d0ad3dca5dd8fd5'

image_dir = app.config['IMAGE_DIRECTORY']

if (app.config['DEBUG'] == "True"):
    app.debug = True
else:
    app.debug = False

basic_auth = BasicAuth(app)

admin = Admin(app,
              name='blueapp',
              template_mode='bootstrap3')

mail = Mail(app)

from database import db

migrate = Migrate(app, db)

from models import GalleryItem, Creator, Product, MailingList
from models import ModelView, ImageView
admin.add_view(ImageView(GalleryItem, db.session))
admin.add_view(ImageView(Product, db.session))
admin.add_view(ModelView(Creator, db.session))
admin.add_view(ModelView(MailingList, db.session))

from views import *

manager = Manager(app)
manager.add_command('db', MigrateCommand)

import blueapp.manage_commands

