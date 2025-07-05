from flask import redirect, render_template, flash, request, url_for
from app.admin import bp
from app.admin.forms import LoginForm
from ..utils import json_handler
from ..models import User
from flask_login import login_required, login_user, current_user, logout_user

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("login"))
    form = LoginForm()
    if request.method == 'POST' and form.validate() and form.password.data == 'pass123':
        user = User(id="admin")
        login_user(user, remember=True)
        flash('Admin login requested!')
        flash('Password data - {}'.format(form.password.data))
        return redirect(url_for("index"))
    return render_template("login.jinja", title="Login", form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@bp.route("/dashboard", methods=['GET'])
@login_required
def dashboard():
    articles = json_handler()
    return render_template('dashboard.jinja', title="Dashboard", articles=articles)
