import os
from flask import Flask
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

working_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(working_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)
application = app

app.config.from_envvar('FLASK_CONFIG')
app.config['SECRET_KEY'] = '60e14db8cbc92633350de1395a54544f5d0ad3dca5dd8fd5'

admin = Admin(app, name='blueapp', template_mode='bootstrap3')

from views import *
from database import db


from models import GalleryItem, User
admin.add_view(ModelView(GalleryItem, db.session))
admin.add_view(ModelView(User, db.session))

manager = Manager(app)

import blueapp.manage_commands

