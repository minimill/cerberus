from flask import (Blueprint, render_template, redirect, url_for, flash,
                   request)
from app.models import User

from flask.ext.login import login_required, logout_user, login_user
from app.forms import LoginForm

users = Blueprint('users', __name__)
PREFIX = 'loginform'


@users.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us.
    form = LoginForm(prefix=PREFIX)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        flash('Welcome, %s.' % user.name)
        return redirect(request.args.get("next") or url_for("admin.index"))

    return render_template('login.html', form=form)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
