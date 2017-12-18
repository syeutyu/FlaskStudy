from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from Login_Test.router import routerInjector


def create_app():
    _app = Flask(__name__)
    CORS(_app)
    JWTManager(_app)
    _app.config.from_json('./config.json')
    routerInjector(_app)
    return _app

app = create_app()