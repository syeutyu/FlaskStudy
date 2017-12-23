from flask_restful import request,Resource
from Login_Test.Mongo.schema import  User
from flask_jwt_extended import *
from flask import jsonify,Response

class SignUp(Resource):
    def get(self):
        response = jsonify({'msg': 'this is get'})
        response.status_code = 200
        return response

    def post(self):
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        User(user_id=user_id,password=password).save()
        return Response('',201)

class Singin(Resource):
    def post(self):
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        find = User.objects(user_id=user_id,password=password)
        if(find):
            response = jsonify(create=create_access_token(identity=password),
                               respresh=create_refresh_token(identity=password))
            response.status_code = 201
            return response
        else :
            return Response('',400)

class PostUser(Resource):
    @jwt_required
    @jwt_refresh_token_required
    def post(self):
