from init_app import app
from flask import render_template
from models import GalleryItem, Product, Creator
from flask.ext.navigation import Navigation
from profile import creatorpage

nav = Navigation(app)
nav.Bar('top', [
    nav.Item('Art', 'gallery'),
    nav.Item('Products', 'products'),
    nav.Item('Creators', 'creators'),
    nav.Item('About', 'about')
])


app.register_blueprint(creatorpage)


@app.template_filter('tagset')
def tag_set(items):
    taglist = []
    for line in [item.tags for item in items]:
        for word in line.split():
            taglist.append(word.strip())
    return set(taglist)

@app.route('/')
@app.route('/index')
def index():
    return render_template('intro.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/creators')
def creators():
    creatorlist = Creator.query.all()
    return render_template('creators.html', creators=creatorlist)

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

@app.route('/shop')
def shop():
    productlist = Product.query.all()    
    return render_template('shop.html', items=productlist)
