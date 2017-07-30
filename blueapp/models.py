from blueapp.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Unicode(127), primary_key=True)
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    

class GalleryItem(db.Model):
    __tablename__ = 'gallery_items'
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information (required for Flask-User)
    name = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    description = db.Column(db.String(511), nullable=False, server_default='')
    # reset_password_token = db.Column(db.String(100), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='1')
    imagefile = db.Column(db.String(511), nullable=False, server_default='')
    thumbfile = db.Column(db.String(511), nullable=False, server_default='')

    def __init__(self, name, description, imagefile, thumbfile):
        self.name = name
        self.description = description
        self.imagefile = imagefile
        self.thumbfile = thumbfile

    def __repr__(self):
        return '<GalleryItem %r>' % self.name


def get_gallery_items():
    items = GalleryItem.query.all()
    return items
