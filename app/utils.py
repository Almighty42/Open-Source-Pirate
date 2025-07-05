from os import environ
from os import path
import json

def read_json(path):
    with open(path) as file_in:
        return json.load(file_in)

def write_json(path, json_data):
    with open(path, 'w') as file_out:
        json.dump(json_data, file_out)

# Loads data.json and returns a valid dictionary
def json_handler():
    project_path = environ.get('PROJECT_PATH')
    if project_path is None:
        raise ValueError("PROJECT PATH environment variable is not set")
    data_path = path.join(project_path, "app/static/data.json")
    json_articles = read_json(data_path )
    articles = list(json_articles.values())
    return articles
