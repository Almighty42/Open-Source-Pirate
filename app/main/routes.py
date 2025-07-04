from flask import render_template, abort
from app.main import bp

@bp.route('/')
@bp.route('/home')
def index():
    
    articles = [
        {
            'id': 23,
            'title': 'My first article',
            'created_at': 'August 7, 2024'
        },
        {
            'id': 45,
            'title': 'My second article',
            'created_at': 'August 8, 2024'
        },
        {
            'id': 11,
            'title': 'My third article',
            'created_at': 'July 27, 2024'
        },
        {
            'id': 101,
            'title': 'My fourth article',
            'created_at': 'August 7, 2024'
        },
    ]

    return render_template('index.jinja', title="Home", articles=articles)

@bp.route('/article/<int:id>')
def article(id):

    articles = [
        {
            'id': 23,
            'title': 'My first article',
            'created_at': 'August 7, 2024'
        },
        {
            'id': 45,
            'title': 'My second article',
            'created_at': 'August 8, 2024'
        },
        {
            'id': 11,
            'title': 'My third article',
            'created_at': 'July 27, 2024'
        },
        {
            'id': 101,
            'title': 'My fourth article',
            'created_at': 'August 7, 2024'
        },
    ]

    article = next((item for item in articles if item['id'] == id), None)
    if not article:
        abort(404)
    return render_template('article.jinja', article=article)
