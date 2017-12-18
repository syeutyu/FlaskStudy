from flask_jwt_extended import *
from flask_restful import request,Resource
from Login_Test.Mongo.schema import  User
from flask import jsonify

class SignUp(Resource):
    def get(self):
        return jsonify({'msg':'this is get'},200)

    def post(self):
        User(id=request.form.get('id'),password=request.form.get('password'))
        response = jsonify({'msg':'success create'})
        response.status_code = 201
        return response
