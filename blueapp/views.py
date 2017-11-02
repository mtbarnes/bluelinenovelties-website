from init_app import app
from flask import render_template, flash, redirect, url_for
from models import GalleryItem, Product, Creator, MailingList
from flask.ext.navigation import Navigation
from profile import creatorpage
from forms import MailingListForm
from init_app import db, mail
from flask_mail import Message
from token import generate_confirmation_token, confirm_token
import datetime

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
@app.route('/index/')
def index():
    return render_template('intro.html')

@app.route('/about/', methods=['GET', 'POST'])
def about():
    mailform = MailingListForm()
    if mailform.validate_on_submit():
        if MailingList.query.filter_by(email=mailform.email.data).first():
            flash('Email %s is already on the list.' %
                  (mailform.email.data), 'danger')
            return redirect(url_for('about'))            
        contact = MailingList(email=mailform.email.data)
        db.session.add(contact)
        db.session.commit()
        token = generate_confirmation_token(mailform.email.data)
        confirmation_url = url_for('confirm_mailinglist', token=token, _external=True)
        msg = Message('Thanks for registering', recipients=[mailform.email.data])
        msg.body = "You're on the Blue Line Novelties mailing list. Use this link to activate yoru account: %s" % (confirmation_url)
        mail.send(msg)
        flash('Email %s confirmed; thanks for signing up! :)' %
              (mailform.email.data), 'info')
        return redirect(url_for('about'))
    return render_template('about.html', mailinglistform=mailform)

@app.route('/creators/')
def creators():
    creatorlist = Creator.query.all()
    return render_template('creators.html', creators=creatorlist)

@app.route('/confirm/mailinglist/<token>')
def confirm_mailinglist(token):
    try:
        email = confirm_token(token)
    except:
        flash('Confirmation link is invalid or expired.', 'danger')
    user = MailingList.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Address confirmed, thanks for signing up.','info')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash("Address confirmed, you're on the list!", 'success')
    return redirect(url_for('index'))

@app.route('/gallery/')
def gallery():
    items = GalleryItem.query.filter_by(visible=True)
    taglist = []
    for line in [item.tags for item in items]:
        for word in line.split():
            taglist.append(word.strip())
    tags = set(taglist)
    return render_template('gallery.html', items=items, tags=tags)

@app.route('/products/', methods=['GET', 'POST'])
def products():
    productlist = Product.query.filter_by(visible=True)
    return render_template('products.html', items=productlist)

@app.route('/shop/')
def shop():
    productlist = Product.query.all()    
    return render_template('shop.html', items=productlist)
