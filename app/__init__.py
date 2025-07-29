from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/*": {"origins": "*"}})  # For dev only — change '*' to allowed origin in production
    app.config.from_object('config.Config')
    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    migrate.init_app(app, db)  # << add this

    from .routes import app as app_routes
    from .roleRegistration import role_registration_routes

    app.register_blueprint(app_routes, url_prefix='/')
    app.register_blueprint(role_registration_routes, url_prefix='/role-registration')

    return app
