from app import db
from models import Pet

db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add Pets
pet1 = Pet(name='derek', species='dog', photo_url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2018/01/12201051/cute-puppy-body-image.jpg',
                age='baby', notes='hello world', available=True)
pet2 = Pet(name='Donnie', species='cat', photo_url='https://www.thesprucepets.com/thmb/6iI33I9cViOCBsbeujMhaVIxv6c=/2304x1728/filters:no_upscale()/close-up-of-cat-lying-on-floor-at-home-908763830-1d61bee6961b45ee8a55bdfa5da1ebb3.jpg',
                age='adult', notes='Adorable cat with a lot of spunk', available=True)
pet3 = Pet(name='Oswald', species='dog', photo_url='https://upload.wikimedia.org/wikipedia/commons/f/fb/Welchcorgipembroke.JPG',
                age='senior', notes='An Old pupper with a love of  love to give', available=True)
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)


db.session.commit()
