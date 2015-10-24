from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import Form
from wtforms import (StringField, PasswordField)
from wtforms_components import PassiveHiddenField
from wtforms.validators import DataRequired, ValidationError, Optional, EqualTo, Regexp
from app.models import Project

BAD_FOLDER = 'Folder name should only contain numbers, letters, and dashes'
ERROR_MSG = 'Incorrect Password'


class ValidPassword():
    """A validator that ensures that there is an Project in the database with
    the filename that is the same as the field's data.
    :param form: The parent form
    :type form: :class:`Form`
    :param field: The field to validate
    :type field: :class:`Field`
    """

    def __init__(self, slug_field_name):
        self.slug_field_name = slug_field_name

    def __call__(self, form, field):
        slug_field = form._fields.get(self.slug_field_name)
        if slug_field is None:
            raise Exception('no field named "%s" in form' %
                            self.other_field_name)
        project = Project.query.filter_by(slug=slug_field.data).first()
        print project, field.data
        if not project:
            raise ValidationError(ERROR_MSG)
        if not check_password_hash(project.password_hash, field.data):
            raise ValidationError(ERROR_MSG)


class RequiredIf(DataRequired):
    # a validator which makes a field required if
    # another field is set and has a truthy value

    def __init__(self, other_field_name, *args, **kwargs):
        self.other_field_name = other_field_name
        super(RequiredIf, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' %
                            self.other_field_name)
        if bool(other_field.data):
            super(RequiredIf, self).__call__(form, field)


class LoginForm(Form):
    slug = PassiveHiddenField('slug')
    password = PasswordField('password',
                             validators=[DataRequired(), ValidPassword('slug')])


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


class EditProjectForm(CreateProjectForm):
    old_slug = PassiveHiddenField('old_slug')
    old_password = PasswordField('old password',
                                 validators=[RequiredIf('password'),
                                             Optional(),
                                             ValidPassword('old_slug')])
    password = PasswordField('new password')
    confirm_password = PasswordField(
        'confirm new password',
        validators=[RequiredIf('password'),
                    EqualTo('password', message='Passwords must match.')])
