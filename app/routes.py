from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():

    articles = [ 
            {
            "title": "USART Protocol explained in detail",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "Embedded",
                "Topic Explained",
                "C Programming"
                ],
            "img": "assets/placeholder.png"
            },

            {
            "title": "RF waves and their relationship with voltages",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "RF",
                "Electronics"
                ],
            "img": "assets/placeholder.png"
            },

            {
            "title": "Hardware abstraction layers and their useses",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "Embedded",
                "Topic Explained"
                ],
            "img": "assets/placeholder.png"
            }
    ]

    projects = [ 
            {
            "title": "FPV Quadcopter drone project",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "Embedded",
                "Robotics"
                ],
            "img": "assets/placeholder.png"
            },

            {
            "title": "Light sensing camera robot project",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "Embedded",
                "Robotics",
                "Python"
                ],
            "img": "assets/placeholder.png"
            },

            {
            "title": "Personal Blog - Open Source Pirate!",
            "body": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.Lorem ipsum dolor sit amet consectetur adipiscing elit...",
            "tags": [
                "Web development",
                "Python"
                ],
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
