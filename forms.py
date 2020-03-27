"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, url


class AddPetForm(FlaskForm):

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", 
                        choices=[('dog','Dog'), ('cat','Cat'),
                        ('porcupine','Porcupine')])
    photo_url = StringField("Photo Url", validators=[Optional(),url()])
    age = SelectField("Age",
                      choices=[('baby', 'Baby'), ('young', 'Young'),
                               ('adult', 'Adult'), ('senior', 'Senior')]
                      )
    notes = StringField("Notes", validators=[Optional()])


