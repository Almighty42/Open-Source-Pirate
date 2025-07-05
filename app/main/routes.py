from flask import render_template, abort
from app.main import bp
import json
from os import environ
from os import path

# TODO: REMOVE THIS ONCE THE DATABASE HAS BEEN IMPLEMENTED

def write_json(path, json_data):
    with open(path, 'w') as file_out:
        json.dump(json_data, file_out)


def read_json(path):
    with open(path) as file_in:
        return json.load(file_in)

# Loads data.json and returns a valid dictionary
def json_handler():
    project_path = environ.get('PROJECT_PATH')
    if project_path is None:
        raise ValueError("PROJECT PATH environment variable is not set")
    data_path = path.join(project_path, "app/static/data.json")
    json_articles = read_json(data_path )
    articles = list(json_articles.values())
    return articles

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
    return render_template('article.jinja', article=article)
