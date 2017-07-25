from flask import Flask
import os
from flask import Flask
from flask import render_template
from flask.ext.navigation import Navigation
from tools import get_gallery_items

working_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(working_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)
application = app

nav = Navigation(app)
import blueapp.views

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('About', 'about'),    
    nav.Item('Gallery', 'gallery'),
    nav.Item('Products', 'products'),
    nav.Item('Philanthropy', 'philanthropy'),
    nav.Item('Sign Up', 'signup')
    ])
