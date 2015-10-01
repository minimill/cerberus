from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import Form
from wtforms import (StringField, PasswordField)
from wtforms_components import PassiveHiddenField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Regexp
from app.models import User, Project

BAD_FOLDER = 'Folder name should only contain numbers, letters, and dashes'
ERROR_MSG = 'Incorrect Password'


def valid_password(form, field):
    """A validator that ensures that there is an image in the database with the
    filename that is the same as the field's data.
    :param form: The parent form
    :type form: :class:`Form`
    :param field: The field to validate
    :type field: :class:`Field`
    """
    project = Project.query.filter_by(slug=form.slug.data).first()
    print project, field.data
    if not project:
        raise ValidationError(ERROR_MSG)
    if not check_password_hash(project.password_hash, field.data):
        raise ValidationError(ERROR_MSG)


class LoginForm(Form):
    slug = PassiveHiddenField('slug')
    password = PasswordField('password',
                             validators=[DataRequired(), valid_password])


class CreateProjectForm(Form):
    slug = StringField('slug')
    name = StringField('name')
    path = StringField('path',
                       validators=[Regexp(r'[\w]([\w-]\/?)+[\w]',
                                          message=BAD_FOLDER)])
    password = PasswordField('password',
                             validators=[DataRequired()])
    confirm_password = PasswordField(
        'repeat password',
        validators=[DataRequired(),
                    EqualTo('password', message='Passwords must match.')])

    def get_password_hash(self):
        if not hasattr(self, '_password_hash'):
            self._password_hash = generate_password_hash(self.password.data)
        return self._password_hash
