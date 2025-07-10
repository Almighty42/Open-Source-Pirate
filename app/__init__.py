import os
from flask import Flask, abort
from config import Config
from flask_login import LoginManager

# Session / Login manager definition
login_manager = LoginManager()
login_manager.login_view = "main.index"

def create_app(test_config = None):
    # Load configuration
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, '...')
    )
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Flask Blueprints
    from app.main import bp as main_bp
    from app.admin import bp as admin_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    # Session / Login manager
    login_manager.init_app(app)
    # Return 404 when a unauthorized user is trying to access a admin only page
    @login_manager.unauthorized_handler
    def unauthorized():
        abort(404)

    return app
