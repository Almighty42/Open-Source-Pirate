from __future__ import print_function
from flask import render_template, abort
from app.main import bp
import json
from os import environ

# TODO: REMOVE THIS ONCE THE DATABASE HAS BEEN IMPLEMENTED

import sys

def write_json(path, json_data):
    with open(path, 'w') as file_out:
        json.dump(json_data, file_out)


def read_json(path):
    with open(path) as file_in:
        return json.load(file_in)

@bp.route('/')
@bp.route('/home')
def index():

    json_articles = read_json(environ.get('PROJECT_PATH') + "app/static/data.json")

    r = json.dumps(json_articles)
    loaded_r = json.loads(r)

    print(json_articles.article_23, file=sys.stderr)

    return render_template('index.jinja', title="Home", articles=loaded_r)

@bp.route('/article/<int:id>')
def article(id):

    articles = [
        {
            'id': 23,
            'title': 'My first article',
            'created_at': 'August 7, 2024',
            'content': 'Hello world'
        },
        {
            'id': 45,
            'title': 'My second article',
            'created_at': 'August 8, 2024',
            'content': 'Hello world 2'
        },
        {
            'id': 11,
            'title': 'My third article',
            'created_at': 'July 27, 2024',
            'content': 'Hello world 3'

        },
        {
            'id': 101,
            'title': 'My fourth article',
            'created_at': 'August 7, 2024',
            'content': 'Hello world 4'
        },
    ]

    article = next((item for item in articles if item['id'] == id), None)
    if not article:
        abort(404)
    return render_template('article.jinja', article=article)
