
# Create DB
from app import create_app
_, db = create_app()
db.drop_all()
db.create_all()

# Save everything
db.session.commit()
