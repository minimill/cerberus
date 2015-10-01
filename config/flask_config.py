import secrets

SECRET_KEY = secrets.SECRET_KEY
META_TITLE = 'Isaac Levien: bassist, composer, and arranger'
META_DESCRIPTION = (
    'Isaac Levien is a bassist, composer, and arranger. He is majoring in Jazz'
    ' Performance at New England Conservatory.'
)
META_NAME = 'Isaac Levien'
META_TWITTER_HANDLE = '@isaaclevien'
META_DOMAIN = 'isaaclevien.com'
META_URL = 'http://' + META_DOMAIN
META_IMAGE = 'img/art.jpg'
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
STATIC_FOLDER_PATH = '/srv/work/private_html/'
