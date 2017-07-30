from init_app import app
from flask_sqlalchemy import SQLAlchemy

def init_db():
    return SQLAlchemy(app)

db = init_db()

