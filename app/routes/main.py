import os
from flask import (Blueprint, render_template, url_for, redirect, abort,
                   send_from_directory)
from flask.ext.login import current_user, login_user
from werkzeug.routing import BaseConverter, ValidationError
from werkzeug.exceptions import HTTPException
from app.forms import CreateProjectForm, LoginForm
from app.models import Project, User
from app import db


class ProjectHashConverter(BaseConverter):

    def to_python(self, value):
        if value == '_':
            raise ValidationError
        project = Project.query.filter_by(slug=value).first()
        if project is None:
            abort(404)
        return project

    def to_url(self, value):
        return value.slug


def add_app_url_map_converter(self, func, name=None):
    """
    Register a custom URL map converters, available application wide.
    :param name: the optional name of the filter, otherwise the function name
                 will be used.
    """
    def register_converter(state):
        state.app.url_map.converters[name or func.__name__] = func

    self.record_once(register_converter)

# monkey-patch the Blueprint object to allow addition of URL map converters
Blueprint.add_app_url_map_converter = add_app_url_map_converter

# create the eyesopen Flask blueprint
main = Blueprint('main', __name__)

main.add_app_url_map_converter(ProjectHashConverter, 'slug')


@main.route('/index.html', methods=['GET'])
@main.route('/', methods=['GET'])
@main.route('/<path:filename>', methods=['GET'])
def root_path(filename=None):
    if current_user.current_project is None:
        return abort(404)
    return redirect(url_for('.project',
                            project=current_user.current_project,
                            route=filename))


@main.route('/<slug:project>/index.html', methods=['GET'])
@main.route('/<slug:project>/', methods=['GET'])
@main.route('/<slug:project>/<path:route>', methods=['GET'])
def project(project, route=None):
    if current_user.current_project != project:
        return redirect(url_for('.authenticate', project=project))
    try:
        if route and route != '/':
            return send_from_directory(project.static_folder, route)
        return send_from_directory(project.static_folder, 'index.html')
    except HTTPException:
        return send_from_directory(project.static_folder,
                                   os.path.join(route, 'index.html'))


@main.route('/_/new/', methods=['GET', 'POST'])
def new():
    print "new"
    form = CreateProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data,
                          slug=form.slug.data,
                          path=form.path.data,
                          password_hash=form.get_password_hash())
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('.project', project=project))

    return render_template('new.html', form=form)


@main.route('/_/authenticate/<slug:project>', methods=['GET', 'POST'])
def authenticate(project):
    print "authenticate"
    print current_user, current_user.is_authenticated()

    if not current_user.is_authenticated():
        print "logging in user"
        user = User()
        db.session.add(user)
        db.session.commit()
        login_user(user)

    if project in current_user.projects:
        print "p:", project
        current_user.current_project = project
        db.session.commit()
        return redirect(url_for('.project', project=project))

    form = LoginForm()
    if form.validate_on_submit():
        print "p:", project
        current_user.current_project = project
        current_user.projects.append(project)
        db.session.commit()
        return redirect(url_for('.project', project=project))

    return render_template('authenticate.html',
                           project=project,
                           form=form)
