from app import db
from models import Pet

db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add Pets
pet1 = Pet(name='derek', species='dog', photo_url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2018/01/12201051/cute-puppy-body-image.jpg',
                age='baby', notes='hello world', available=True)


db.session.add(pet1)
db.session.commit()
