from init_app import app
from flask import render_template
from models import get_gallery_items, get_gallery_tags
from flask.ext.navigation import Navigation

nav = Navigation(app)
nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('About', 'about'),    
    nav.Item('Gallery', 'gallery'),
    nav.Item('Products', 'products'),
    nav.Item('Philanthropy', 'philanthropy'),
    nav.Item('Sign Up', 'signup')
])


@app.route('/')
@app.route('/index')
def index():
    return render_template('intro.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    items = get_gallery_items()
    tags = get_gallery_tags()
    return render_template('gallery.html', items=items, tags=tags)

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/philanthropy')
def philanthropy():
    return render_template('philanthropy.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')
