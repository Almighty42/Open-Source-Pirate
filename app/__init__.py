from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.main import bp as main_bp
    from app.admin import bp as admin_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app
