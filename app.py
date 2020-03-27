"""Flask app for adopt app."""

from flask import Flask, render_template, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm


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
    pets = Pet.query.all()
    return render_template('pet-listing.html', pets=pets)


@app.route('/add', methods=["POST", "GET"])
def add_pet():

    form = AddPetForm()


    if form.validate_on_submit():
        pet_name = form.name.data
        species = form.species.data
        
        validate_species(form,species)

        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data or None

        new_pet = Pet(name=pet_name,
                      species=species,
                      photo_url=photo_url,
                      age=age,
                      notes=notes
                      )
        db.session.add(new_pet)
        db.session.commit()
    else:
        return render_template("add-pet.html",
                               form=form)

    return redirect("/")

@app.route('/<int:pet_id>')
def pet_details(pet_id):
    current_pet = Pet.query.get_or_404(pet_id)
    
    return render_template('pet-details.html', pet=current_pet)