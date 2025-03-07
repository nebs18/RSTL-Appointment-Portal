from flask import Flask
from app.routes.metrology import metrology
from app.routes.main import main
from app.routes.admin import admin


def create_app(config_filename=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'change-this-secret-key'
    if config_filename:
        app.config.from_pyfile(config_filename)
    
    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(metrology)
    app.register_blueprint(admin)
    return app
 