from blueapp.database import db
from flask_admin.contrib import sqla
from init_app import app, basic_auth
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Response
from flask_admin import form
from init_app import image_dir
from jinja2 import Markup
from flask import url_for

class AuthException(HTTPException):
    def __init__(self, message):
        super(AuthException, self).__init__(message, Response(
            "Not authenticated, refresh the page or fuck off.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class ModelView(sqla.ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


    
# class User(db.Model, UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Unicode(127), primary_key=True)
#     email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
#     password = db.Column(db.String(255), nullable=False, server_default='')

#     def __init__(self, id):
#         self.id = id

class GalleryItem(db.Model):
    __tablename__ = 'gallery_items'
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information (required for Flask-User)
    name = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    description = db.Column(db.String(511), nullable=False, server_default='')
    # reset_password_token = db.Column(db.String(100), nullable=False, server_default='')
    tags = db.Column(db.String(255), nullable=False, server_default='')
    creator = db.Column(db.Unicode(127), nullable=False, server_default=u'')
    active = db.Column(db.Boolean(), nullable=False, server_default='1')
    imagefile = db.Column(db.String(511), nullable=False, server_default='')
    thumbfile = db.Column(db.String(511), nullable=False, server_default='')



class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Unicode(255), nullable=False, server_default=u'')
    description = db.Column(db.Unicode(511), nullable=False, server_default=u'')
    tags = db.Column(db.String(255), nullable=False, server_default='')
    creator = db.Column(db.Unicode(127), nullable=False, server_default=u'')
    imagefile = db.Column(db.String(511), nullable=False, server_default='')
    quantity = db.Column(db.Integer(), nullable=False, server_default='1')
    deliverable = db.Column(db.Boolean(), nullable=False, server_default='0')
    price = db.Column(db.String(31), nullable=False, server_default="0.00")


class ProductView(sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.imagefile:
            return ''

        return Markup('<img src="%s">' %
                      url_for('static',
                              filename="img/"+form.thumbgen_filename(model.imagefile)))
    column_formatters = {
        'imagefile' : _list_thumbnail
    }

    form_extra_fields = {
        'imagefile' : form.ImageUploadField('Image',
                                       base_path=image_dir,
                                       thumbnail_size=(100, 100, True))
    }



# class Creator(db.Model):
#     __tablename__ = 'creators'


