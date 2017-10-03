from blueapp.database import db
import datetime

# class User(db.Model, UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Unicode(127), primary_key=True)
#     email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
#     password = db.Column(db.String(255), nullable=False, server_default='')

#     def __init__(self, id):
#         self.id = id

class MailingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(63), unique=True)
    confirmed = db.Column(db.Boolean, nullable=False, server_default='0')
    confirmed_on = db.Column(db.DateTime, nullable=True)
    registered_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, **kwargs):
        super(MailingList, self).__init__(**kwargs)
        self.registered_on = datetime.datetime.now()

    def __repr__(self):
        return self.email

    
class Creator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))
    gallery_items = db.relationship('GalleryItem', backref='creator',
                                    lazy='dynamic')
    products = db.relationship('Product', backref='creator', lazy='dynamic')
    bio = db.Column(db.String(1023), nullable=False, server_default='')
    username = db.Column(db.String(31), nullable=False, unique=True)

    def __repr__(self):
        return self.username
    

class GalleryItem(db.Model):
    __tablename__ = 'gallery_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    description = db.Column(db.String(511), nullable=False, server_default='')
    imagefile = db.Column(db.String(511), nullable=False, server_default='')
    creator_id = db.Column(db.Integer, db.ForeignKey('creator.id'))
    tags  = db.Column(db.String(511), nullable=False, server_default='')

    def __repr__(self):
        return "%s : %s" % (self.name, self.id)
    

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255), nullable=False, server_default=u'')
    description = db.Column(db.Unicode(511), nullable=False, server_default=u'')
    tags  = db.Column(db.String(511), nullable=False, server_default='')
    creator_id = db.Column(db.Integer, db.ForeignKey('creator.id'))
    imagefile = db.Column(db.String(511), nullable=False, server_default='')
    quantity = db.Column(db.Integer(), nullable=True, server_default='1')
    deliverable = db.Column(db.Boolean(), nullable=False, server_default='0')
    price = db.Column(db.String(31), nullable=False, server_default="0.00")
    weight = db.Column(db.Float(), nullable=True, server_default="0.0")
    dimensions = db.Column(db.String(127), nullable=True)
    
    def __repr__(self):
        return "%s - DBID:%s" % (self.name, self.id)
    

