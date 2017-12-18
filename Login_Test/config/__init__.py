from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from Login_Test.router import routerInjector
from Login_Test.Mongo import connection_db


def create_app():
    _app = Flask(__name__)
    CORS(_app)
    JWTManager(_app)
    _app.config.from_json('./config.json')
    routerInjector(_app)
    connection_db(_app)
    return _app

app = create_app()