from flask import Flask
from sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    app.secret_key = "supersecrete"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    