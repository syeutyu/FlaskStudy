from flask_restful import Resource,abort
from flask import request

class CreateUser(Resource):
    def get(self):
        print('실행합니당')
        data = request.args["data"]
        return {'status': data}
    def post(self):
        abort(400)