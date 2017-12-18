from flask_jwt_extended import *
from flask_restful import request,Resource
from Login_Test.Mongo.schema import  User
from flask import jsonify

class SignUp(Resource):
    def get(self):
        response = jsonify({'msg': 'this is get'})
        response.status_code = 200
        return response

    def post(self):
        User(user_id=request.form.get('id'),password=request.form.get('password')).save()
        response = jsonify({'msg':'success create'})
        response.status_code = 201
        return response
