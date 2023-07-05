from flask import Flask
from app.config import config_by_name
import mysql.connector

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    global db
    db = mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )

    with app.app_context():
        from app.routes.users import users_bp

        app.register_blueprint(users_bp)

        return app
