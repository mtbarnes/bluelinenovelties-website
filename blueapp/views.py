from init_app import app
from flask import render_template, flash, redirect
from models import GalleryItem, Product, Creator, MailingList
from flask.ext.navigation import Navigation
from profile import creatorpage
from forms import MailingListForm
from init_app import db, mail
from flask_mail import Message

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

# Add mailing list form to every template

@app.route('/')
@app.route('/index')
def index():
    return render_template('intro.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = MailingListForm()
    if form.validate_on_submit():
        if MailingList.query.filter_by(email=form.email.data).first():
            flash('Email %s is already on the list.' %
                  (form.email.data), 'danger')
            return redirect('/about')            
        contact = MailingList(email=form.email.data)
        db.session.add(contact)
        db.session.commit()
        msg = Message('Thanks for registering', recipients=[form.email.data])
        msg.body = "You're on the Blue Line Novelties mailing list."
        mail.send(msg)
        flash('Email %s confirmed; thanks for signing up! :)' %
              (form.email.data), 'info')
        return redirect('/about')
    return render_template('about.html', form=form)

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

@app.route('/products', methods=['GET', 'POST'])
def products():
    productlist = Product.query.all()
    form = MailingListForm()
    if form.validate_on_submit():
        if MailingList.query.filter_by(email=form.email.data).first():
            flash('Email %s is already on the list.' %
                  (form.email.data), 'danger')
            return redirect('/products')            
        contact = MailingList(email=form.email.data)
        db.session.add(contact)
        db.session.commit()
        msg = Message('Thanks for registering', recipients=[form.email.data])
        msg.body = "You're on the Blue Line Novelties mailing list."
        mail.send(msg)
        flash('Email %s confirmed; thanks for signing up! :)' %
              (form.email.data), 'info')
        return redirect('/products')
    return render_template('products.html', items=productlist, form=form)

@app.route('/shop')
def shop():
    productlist = Product.query.all()    
    return render_template('shop.html', items=productlist)
