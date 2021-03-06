from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from sys import argv

app = None
db = None
login_manager = None


def create_app():
    global app
    global db
    global login_manager

    # Flask
    app = Flask(__name__,
                static_folder='static/dist/',
                static_url_path='/static')
    app.config.from_object('config.flask_config')

    # SQLAlchemy
    db = SQLAlchemy(app)

    # Login
    login_manager = LoginManager(app)
    login_manager.login_view = 'users.login'

    # Debug
    app.config['DEBUG'] = (len(argv) == 2 and argv[1] == 'debug')

    @login_manager.user_loader
    def load_user(userid):
        from models import User
        return User.query.get(userid)

    from app.models import AnonymousUser
    login_manager.anonymous_user = AnonymousUser

    register_blueprints(app)
    return app, db


def register_blueprints(app):
    from app.routes import main
    app.register_blueprint(main)
