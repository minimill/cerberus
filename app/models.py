import random
import string
from app import db
from flask.ext.login import UserMixin, AnonymousUserMixin

authentications = db.Table(
    'authentications',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    path = db.Column(db.String(80))
    password_hash = db.Column(db.String(80))

    def __init__(self, name, path, password_hash, slug=None):
        self.name = name
        self.path = path
        self.password_hash = password_hash
        self.slug = slug if slug is not None else self._generate_slug()

    def _generate_slug(self, length=8):
        return ''.join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits) for _ in range(length))

    @property
    def static_folder(self):
        return '/Users/dan/working/' + self.path


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    projects = db.relationship('Project',
                               secondary=authentications,
                               backref=db.backref('users', lazy='dynamic'))
    current_project = db.relationship("Project",
                                      foreign_keys="User.current_project_id")
    current_project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __repr__(self):
        return '<User %r>' % self.id


class AnonymousUser(AnonymousUserMixin):
    current_project = None
