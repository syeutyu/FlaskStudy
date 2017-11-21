from flask import Flask,Blueprint
from flask_restful import  Api
from RestAPI.testClass import CreateUser

blueprint =Blueprint('createUser',__name__)
api = Api(blueprint) # bluePrint 객체 파라미터 넣어줌
api.add_resource(CreateUser, '/user')

app = Flask(__name__)
app.register_blueprint(blueprint)


if __name__ == '__main__':
    """
        :rtype: Flask
        """

    app.run(debug=True)