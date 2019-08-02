from flask_admin.contrib import sqla
from init_app import app, basic_auth, mail
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Response
from flask_admin import form
from init_app import image_dir
from jinja2 import Markup
from flask import url_for, flash, render_template, redirect
from sqlalchemy.event import listens_for
from subprocess import call
import uuid
from werkzeug.utils import secure_filename
import os
from flask_admin import BaseView, expose
from forms import SendMailForm
from flask_mail import Message
from models import GalleryItem, Product, MailingList

def _imagename_uuid1_gen(obj, file_data):
    doo, ext = os.path.splitext(file_data.filename)
    uid = uuid.uuid1()
    return secure_filename('{}{}'.format(uid, ext))


class AuthException(HTTPException):
    def __init__(self, message):
        super(AuthException, self).__init__(message, Response(
            "Not authenticated, refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))



class EmailView(BaseView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        form = SendMailForm()
        if form.validate_on_submit():
            result = MailingList.query.filter_by(confirmed=True)
            addresslist = [item.email for item in result]
            for address in addresslist:
                msg = Message(str(form.title.data), recipients=[address])
                message = {'title' : form.title.data,
                           'subtitle' : form.subtitle.data,
                           'content' : form.content.data
                }
                msg.html = render_template('email/email_base.html', message=message)
                mail.send(msg)
            flash('Email %s sent' %
                  (form.title.data), 'info')
            return redirect('/admin')
        return self.render('email_index.html', form=form)

class ModelView(sqla.ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


    
class ImageView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.imagefile:
            return ''
        # This is a horrible kludge!
        full_filename = "img/"+form.thumbgen_filename(model.imagefile)
        return Markup('<img src="%s">' %
                      url_for('static',
                              filename=full_filename))
    column_formatters = {
        'imagefile' : _list_thumbnail
    }

    column_editable_list = ['visible', 'tags', 'name', 'tags']
    
    form_extra_fields = {
        'imagefile' : form.ImageUploadField('Image',
                                            base_path=image_dir,
                                            thumbnail_size=(100, 100, True),
                                            namegen=_imagename_uuid1_gen)
    }



@listens_for(Product, "after_insert")
@listens_for(Product, "after_update")
@listens_for(GalleryItem, "after_insert")
@listens_for(GalleryItem, "after_update")
def resize_image(mapper, connection, target):
    image_location = image_dir + target.imagefile
    call(['bash', image_dir+'imgoptim.sh', image_location])
    

@listens_for(Product, "after_delete")
@listens_for(GalleryItem, "after_delete")
def delete_image(mapper, connection, target):
    image_location = image_dir + target.imagefile
    thumb_location = image_dir + form.thumbgen_filename(target.imagefile)
    try:
        os.remove(image_location)
    except OSError:
        pass
    try:
        os.remove(thumb_location)
    except OSError:
        pass
