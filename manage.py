import getpass
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

# Create DB
from app import create_app
_, db = create_app()
db.drop_all()
db.create_all()

# # Create Users
# USERS = [
#     ('Isaac Levien', 'isaaclevien@mac.com'),
#     ('Dan Schlosser', 'dan@schlosser.io')
# ]
# from app.models import User, Recordings, Bio, Gig

# for name, email in USERS:
#     print 'Creating user {} <{}>'.format(name, email)
#     password = getpass.getpass()
#     user = User(name=name,
#                 email=email,
#                 password_hash=generate_password_hash(password))
#     db.session.add(user)

# # Create Recordings
# recordings = Recordings(items=', '.join([
#     'https://soundcloud.com/chris-mccarthy-1/doldrums'
# ]))
# db.session.add(recordings)

# # Create Bios
# SHORT_BIO = ('Isaac Levien is a bassist, composer, and arranger'
#              ' living in Boston.  He grew up in Lexington, MA, '
#              'and will graduate from New England Conservatory '
#              'with a B.A. in Jazz Bass Performance in 2016.')
# LONG_BIO = SHORT_BIO + ' He is a great guy.'
# BANDS = 'Band One, Band Two.'
# TAGLINE = 'bassist, composer, teacher, and arranger'

# bio = Bio(tagline=TAGLINE, short_bio=SHORT_BIO, long_bio=LONG_BIO, bands=BANDS)
# db.session.add(bio)

# # Create Gigs
# gig_date = datetime.now() + timedelta(days=1)
# gig = Gig(date=gig_date.date(), time=gig_date.time(), location="The Lillypad",
#           band="Saw Mill", details="It's going to be a *great* event.")
# db.session.add(gig)

# Save everything
db.session.commit()
