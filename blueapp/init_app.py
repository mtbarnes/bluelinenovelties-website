import os
from flask import Flask
from flask.ext.navigation import Navigation
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

working_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(working_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)
application = app

app.config.from_envvar('FLASK_CONFIG')
app.config['SECRET_KEY'] = '60e14db8cbc92633350de1395a54544f5d0ad3dca5dd8fd5'

db = SQLAlchemy(app)

from views import *

nav = Navigation(app)
nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('About', 'about'),    
    nav.Item('Gallery', 'gallery'),
    nav.Item('Products', 'products'),
    nav.Item('Philanthropy', 'philanthropy'),
    nav.Item('Sign Up', 'signup')
])

manager = Manager(app)

import blueapp.manage_commands
