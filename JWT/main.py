from flask import Flask,request,jsonify
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,jwt_refresh_token_required,get_jwt_identity,JWTManager
from mongo.schema import mongoengine
from bson.json_util import dumps
app = Flask(__name__)
app.config.update(
    SECRET_KEY='super secret',
    JWT_HEADER_TYPE='JWT'
)

JWTManager(app)

@app.route('/create',methods=['POST'])
def create():
    u = mongoengine.objects()
    a = u[0].test_num
    print(a)
    print(type(a))

    return jsonify({
        'msg' : create_access_token(a)
    })


@app.route('/change')
@jwt_required
def protected():
     re = request.args.get('t')
     user = mongoengine.objects(test_num=get_jwt_identity()).update(test_num=re)
     if user:
         print('존재')
     else :
         print('발견 X')
     return 'test'

if __name__ =='__main__':
    app.run(debug=True)