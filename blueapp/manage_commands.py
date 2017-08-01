import datetime

from blueapp.init_app import app, db, manager
from blueapp.models import GalleryItem


@manager.command
def init_db():
    """ Initialize the database."""
    # Create all tables
    db.create_all()

@manager.command
def fill_db():
    # Add all Users
    add_items()
    

def add_items():
    """ Create users when app starts """
    items = init_gallery_items()
    for item in items:
        find_or_create_item(item['name'], item['description'],
                            item['imagefile'], item['thumbfile'])
    db.session.commit()


def find_or_create_item(name, description, imagefile, thumbfile):
    """ Find existing item or create new item """
    item = GalleryItem.query.filter(GalleryItem.name == name).first()
    if not item:
        item = GalleryItem(
            name = name,
            description = description,
            imagefile = imagefile,
            thumbfile = thumbfile)
        db.session.add(item)
    return item


def init_gallery_items():
    items = []
    items.append(dict([('name', u'Calcite in Limestone'),
                       ('imagefile', 'img/portfolio/large/01.jpg'),
                       ('thumbfile', 'img/portfolio/thumb/01.jpg'),
                       ('tags', 'calcite crystals limestone'),
                       ('description', u'Beautiful calcite crystal from Jollyville, Texas.')]))
    items.append(dict([('name', u'Small Calcite Crystals'),
                       ('imagefile', 'img/portfolio/large/02.jpg'),
                       ('thumbfile', 'img/portfolio/thumb/02.jpg'),
                       ('tags', 'calcite crystals'),
                       ('description', u'These samples clearly show the distinctive Calcite crystal lattice.')]))
    items.append(dict([('name', u'UMOs'),
                       ('imagefile', 'img/portfolio/large/03.jpg'),
                       ('thumbfile', 'img/portfolio/thumb/03.jpg'),
                       ('tags', 'ufopoop'),
                       ('description', u'Unidentified Metallic Objects found in the Slaughter Lane area.')]))
    items.append(dict([('name', u'Metallic Meteorite'),
                       ('imagefile', 'img/portfolio/large/04.jpg'),
                       ('thumbfile', 'img/portfolio/thumb/04.jpg'),
                       ('tags', 'meteorites ufopoop'),
                       ('description', u'A dense metallic object thought by some to be a meteorite.')]))
    items.append(dict([('name', u'Calcite on Limestone Matrix'),
                       ('imagefile', 'img/portfolio/large/05.jpg'),
                       ('thumbfile', 'img/portfolio/thumb/05.jpg'),
                       ('tags', 'calcite crystals'),
                       ('description', u'Beautiful Calcite cluster on a limestone matrix from Cedar Park, Texas')]))
    items.append(dict([('name', u'UFO parts'),
                       ('imagefile', 'img/portfolio/large/06.jpg'),
                       ('thumbfile', 'img/portfolio/thumb/06.jpg'),
                       ('tags', 'meteorites ufopoop'),
                       ('description', u'Metallic objects of unknown origin, believed by some to be UFO parts.')]))
    items.append(dict([('name', u'Fossilized Coral'),
                       ('imagefile', 'img/portfolio/large/07.jpg'),
                       ('thumbfile', 'img/portfolio/thumb/07.jpg'),
                       ('tags', 'fossils'),
                       ('description', u'Fossils of aquatic origin found in the Lake Creek area.')]))
    items.append(dict([('name', u'Unknown Fossil'),
                       ('imagefile', 'img/portfolio/large/08.jpg'),
                       ('thumbfile', 'img/portfolio/thumb/08.jpg'),
                       ('tags', 'fossils'),
                       ('description', u'Unknown fossil, possibly aquatic, found near shells in north Austn.')]))
    return items
