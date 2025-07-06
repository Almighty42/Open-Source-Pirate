from flask import redirect, render_template, flash, request, url_for
from app.admin import bp
from app.admin.forms import ArticleForm, LoginForm
from ..utils import json_handler
from ..models import User
from flask_login import login_required, login_user, current_user, logout_user
from datetime import datetime

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if request.method == 'POST' and form.validate() and form.password.data == 'pass123':
        user = User(id="admin")
        login_user(user, remember=True)
        flash('Admin login requested!')
        flash('Password data - {}'.format(form.password.data))
        return redirect(url_for("main.index"))
    is_auth = current_user.is_authenticated
    return render_template("login.jinja", title="Login", form=form, is_auth=is_auth)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@bp.route("/dashboard")
@login_required
def dashboard():
    articles = json_handler()
    is_auth = current_user.is_authenticated
    return render_template('dashboard.jinja', title="Dashboard", articles=articles, is_auth=is_auth)

@bp.route("/new", methods=['GET', 'POST'])
@login_required
def new():
    form = ArticleForm()
    if request.method == 'POST' and form.validate():
        # Code that adds a new article to the data.json DB
        flash('New article added! - article title {}'.format(form.title.data))
        return redirect(url_for("main.index"))
    form.pub_date.data = datetime.now().strftime('%d-%m-%Y')
    is_auth = current_user.is_authenticated
    return render_template('new.jinja', title="Add new article", form=form, is_auth=is_auth)
