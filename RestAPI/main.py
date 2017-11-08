from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    def get(self):
        print('실행합니당')
        data = request.args["data"]
        return {'status': data}

api.add_resource(CreateUser, '/user')

if __name__ == '__main__':
    """
        :rtype: Flask
        """
    app.run(debug=True)