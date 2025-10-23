# Builds Flask app with database and routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourpass@localhost:5432/books_data'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .SearchBooksWeb import main_bp
    app.register_blueprint(main_bp)

    from .api import api_bp  # Add the API blueprint
    app.register_blueprint(api_bp)

    return app



  
