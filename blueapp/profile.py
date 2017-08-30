from flask import Blueprint, render_template, g
from models import Creator

creatorpage = Blueprint('creatorpage', __name__, url_prefix='/creator/<username>')

@creatorpage.url_value_preprocessor
def get_creator(endpoint, values):
    query = Creator.query.filter_by(username=values.pop('username'))
    g.creator = query.first_or_404()

@creatorpage.route('/')
def index():
    # query = Creator.query.filter_by(id=id)
    # g.creator = query.first_or_404()
    return render_template('creatorpage/index.html')

@creatorpage.route('/gallery')
def gallery():
    return render_template('creatorpage/gallery.html')

