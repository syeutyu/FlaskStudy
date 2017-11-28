from flask import Flask
from flask_cors import CORS

cors = CORS()

def createApp():
    """
    flask instance create and another program install
    :return: Flask
    """
    application = Flask(__name__)
    application.config.from_pyfile('./config.py') # flask 인스턴스의 설정값으로 py 파일 불러와서 설정

    cors.init_app(application)

    return application
app = createApp()

