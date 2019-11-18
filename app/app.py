from flask import Flask
from app.v1 import create_blueprint_v1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
    return app
