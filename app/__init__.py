from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.blueprints.main import bp as main_bp
        app.register_blueprint(main_bp)
        
        from app.blueprints.authentication import bp as authentication_bp
        app.register_blueprint(authentication_bp)

        from app.blueprints.main import errors

    return app
