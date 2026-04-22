from flask import Flask
from .config import Config
from .extensions import db, login_manager, bcrypt, migrate, limiter
from .auth.routes import auth_bp
from .main.routes import main_bp
from .posts.routes import posts_bp
from .admin.routes import admin_bp
from .reports.routes import reports_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

    # blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(admin_bp)

    return app
