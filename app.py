"""Flask app for adopt app."""

from flask import Flask, render_template, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    """goes to our main pet listing page"""
    pets = Pet.query.all()
    return render_template('pet-listing.html', pets=pets)


@app.route('/add', methods=["POST", "GET"])
def add_pet():

    """goes to our add pet form and handles add pet event!"""


    form = AddPetForm()


    if form.validate_on_submit():
        pet_name = form.name.data
        species = form.species.data
        

        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data or None

        new_pet = Pet(name=pet_name,
                      species=species,
                      photo_url=photo_url,
                      age=age,
                      notes=notes,
                      )
        db.session.add(new_pet)
        db.session.commit()
    else:
        return render_template("add-pet.html",
                               form=form)

    return redirect("/")

@app.route('/<int:pet_id>', methods=["POST","GET"])
def pet_details(pet_id):
    """takes us to our pet  detail page and handles edit if info is  edited!"""

    current_pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data or None
        available = form.available.data

        if photo_url is not None:
            current_pet.photo_url = photo_url

        current_pet.age = age
        current_pet.notes = notes
        current_pet.available =  available

        db.session.commit()

    else:
        return render_template('pet-details.html', pet=current_pet, form=form)
    
    return redirect("/")