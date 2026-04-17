from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/articles")
def articles():
    return render_template("articles.html")

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/about")
def about():
    return render_template("about.html")
