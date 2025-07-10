from flask import render_template, abort
from flask_login import current_user
from app.main import bp
# TODO: REMOVE THIS ONCE THE DATABASE HAS BEEN IMPLEMENTED
from ..utils import data_handler

@bp.route('/')
@bp.route('/home')
def index():
    articles = data_handler()
    is_auth = current_user.is_authenticated
    return render_template('index.jinja', title="Home", articles=articles, is_auth=is_auth)

@bp.route('/article/<int:id>')
def article(id):
    articles = data_handler()
    article = next((item for item in articles if item['id'] == id), None)
    is_auth = current_user.is_authenticated
    if not article:
        abort(404)
    return render_template('article.jinja', title="Article", article=article, is_auth=is_auth)
