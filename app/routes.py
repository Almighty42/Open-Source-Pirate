from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():

    articles = [
            {
                "category": "Software Development / Embedded",
                "title": "Use of AI in Embedded Development",
                "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit. \n\n Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
                "tags": [
                    "Embedded",
                    "Topic Explained",
                    "C Programming"
                ],
                "date": "02 APR 2026",
                "read_time": "12 MIN READ"
            },
            {
                "category": "Electronics",
                "title": "How to use a solder properly",
                "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit. \n\n Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
                "tags": [
                    "Electronics",
                    "Hands-on"
                ],
                "date": "13 JAN 2026",
                "read_time": "9 MIN READ"
            }
    ]

    projects = [ 
            {
            "title": "USART Driver from scratch",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit. \n\n Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "Embedded",
                "Topic Explained",
                "C Programming"
                ],
            "category": "Software development / Embedded",
            "img": "assets/placeholder.png"
            },

            {
            "title": "Custom RF emmiter",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit. \n\n Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "RF",
                "Electronics"
                ],
            "category": "Hardware development / RF",
            "img": "assets/placeholder.png"
            },

            {
            "title": "SPI Driver from scratch",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit. \n\n Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "Embedded",
                "Topic Explained"
                ],
            "category": "Software development / Embedded",
            "img": "assets/placeholder.png"
            }
    ]

    return render_template("index.html", articles=articles, projects=projects)

@main.route("/articles")
def articles():
    return render_template("articles.html")

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/about")
def about():
    return render_template("about.html")
