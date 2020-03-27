"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    '''Pets Model'''

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String,
                     nullable=False)
    species = db.Column(db.String,
                     nullable=False)
    photo_url = db.Column(db.String,
                     default='https://www.amigonaosecompra.com.br/assets/fallback/thumb_default_pet-675f19f8212c0176eb193a2110351fdf91eb20408d9d6e5ecd796310c49c11ba.png')
    age = db.Column(db.String,
                     nullable=False) 
    notes = db.Column(db.String)              
    available = db.Column(db.Boolean,
                     default=True) 