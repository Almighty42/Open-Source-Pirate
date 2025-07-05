from flask import render_template, abort
from app.main import bp
# TODO: REMOVE THIS ONCE THE DATABASE HAS BEEN IMPLEMENTED
from ..utils import json_handler

@bp.route('/')
@bp.route('/home')
def index():
    articles = json_handler()
    return render_template('index.jinja', title="Home", articles=articles)

@bp.route('/article/<int:id>')
def article(id):
    articles = json_handler()
    article = next((item for item in articles if item['id'] == id), None)
    if not article:
        abort(404)
    return render_template('article.jinja', title="Article", article=article)
