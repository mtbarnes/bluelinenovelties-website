from init_app import app
from flask import render_template
from models import GalleryItem, Product
from flask.ext.navigation import Navigation

nav = Navigation(app)
nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Gallery', 'gallery'),
    nav.Item('Products', 'products'),
    nav.Item('About', 'about'),    
    nav.Item('Social', 'signup')
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
    items = GalleryItem.query.all()
    taglist = []
    for line in [item.tags for item in items]:
        for word in line.split():
            taglist.append(word.strip())
    tags = set(taglist)
    return render_template('gallery.html', items=items, tags=tags)

@app.route('/products')
def products():
    productlist = Product.query.all()
    return render_template('products.html', items=productlist)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')
