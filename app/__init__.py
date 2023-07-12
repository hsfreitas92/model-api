from flask import Flask
from app.config import config_by_name
import mysql.connector

app = Flask(__name__)

def create_db_connection():
    db = mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )
    return db

def create_app(config_name):
    app.config.from_object(config_by_name[config_name])
    create_db_connection()

    with app.app_context():
        from app.routes.users import users_bp
        app.register_blueprint(users_bp)
        return app
