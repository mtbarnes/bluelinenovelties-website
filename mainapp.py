from flask import Flask
from flask import render_template
from flask.ext.navigation import Navigation
from tools import get_gallery_items

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



if __name__ == '__main__':
    app.run(debug=True, port=3535, host='0.0.0.0')
