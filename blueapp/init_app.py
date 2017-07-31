import os
from flask import Flask
from flask_script import Manager
from flask_admin import Admin
from flask_sslify import SSLify
from flask_basicauth import BasicAuth

working_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(working_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)
application = app
# sslify = SSLify(app)

app.config.from_envvar('FLASK_CONFIG')
app.config['SECRET_KEY'] = '60e14db8cbc92633350de1395a54544f5d0ad3dca5dd8fd5'

if (app.config['DEBUG'] == "True"):
    app.debug = True
else:
    app.debug = False

basic_auth = BasicAuth(app)
admin = Admin(app, name='blueapp', template_mode='bootstrap3')

from views import *
from database import db


from models import GalleryItem, ModelView
admin.add_view(ModelView(GalleryItem, db.session))


manager = Manager(app)

import blueapp.manage_commands

