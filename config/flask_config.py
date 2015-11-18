from sys import stderr

try:
    import secrets

    SECRET_KEY = secrets.SECRET_KEY
    META_TITLE = 'Cerberus: secure static hosting made by Minimill.'
    META_DESCRIPTION = (
        'Cerberus: secure static hosting made by Minimill.'
    )
    META_NAME = 'Cerberus'
    META_TWITTER_HANDLE = '@minimill_co'
    META_DOMAIN = 'work.minimill.co'
    META_URL = 'http://' + META_DOMAIN
    META_IMAGE = 'img/lock.svg'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    STATIC_FOLDER_PATH = '/srv/work/private_html/'

except ImportError:
    print >> stderr, 'Could not find config/secrets.py.  Do you have one?'
    exit(1)

except AttributeError as e:
    attr = e.message.lstrip('\'module\' object has no attribute ').rstrip('\'')
    print >> stderr, 'config/secrets.py is missing the key "%s"' % attr
    exit(1)
