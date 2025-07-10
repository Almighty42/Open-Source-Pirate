from flask import redirect, render_template, flash, request, url_for, abort
from app.admin import bp
from app.admin.forms import ArticleForm, LoginForm
from ..utils import data_handler, data_update
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
    articles = data_handler()
    is_auth = current_user.is_authenticated
    return render_template('dashboard.jinja', title="Dashboard", articles=articles, is_auth=is_auth)

@bp.route("/new", methods=['GET', 'POST'])
@login_required
def new():
    form = ArticleForm()
    if request.method == 'POST' and form.validate():
        # Load articles from DB
        articles = data_handler()
        # New article definition
        new_article = {
            "id": max([article["id"] for article in articles], default=0) + 1,
            "title": form.title.data,
            "created_at": datetime.now().strftime('%B %d, %Y'),
            "content": form.content.data
        }
        # Add new article to the local copy of articles DB
        articles.append(new_article)
        # Write copy to the DB
        data_update(articles)
        # Finished!
        flash('New article added! - article title {}'.format(form.title.data))
        return redirect(url_for("main.index"))
    form.pub_date.data = datetime.now().strftime('%B %d, %Y')
    is_auth = current_user.is_authenticated
    return render_template('new.jinja', title="Add new article", form=form, is_auth=is_auth)

@bp.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    form = ArticleForm()
    articles = data_handler()
    article = next((article for article in articles if article['id'] == id), None)
    if article is None:
        abort(404)
    if request.method == 'GET':
        form.title.data = article['title']
        form.pub_date.data = article['created_at']
        form.content.data = article['content']
    elif request.method == 'POST' and form.validate():
        article['title'] = form.title.data
        article['content'] = form.content.data
        data_update(articles)
        flash("Article updated successfully!")
        return redirect(url_for('main.index'))
    is_auth = current_user.is_authenticated
    return render_template('edit.jinja', title="Edit a article", form=form, is_auth=is_auth, article=article)

@bp.route("/delete/<int:id>", methods=['POST'])
@login_required
def delete(id):
    articles = data_handler()
    article = next((article for article in articles if article['id'] == id), None)
    if article is None:
        abort(404)
    else:
        articles.remove(article)
        data_update(articles)
        flash(f'Article {id} deleted successfully!')
        return redirect(url_for('admin.dashboard'))
