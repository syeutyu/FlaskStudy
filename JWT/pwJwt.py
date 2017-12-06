import jwt
from flask import Flask,request,jsonify

app = Flask(__name__)

staticValue = 'test'
@app.route('/',methods=['POST'])
def post():
    print('접속')
    staticValue = jwt.encode({request.form.get('test'):'payload'},'secret key',algorithm='HS256')
    print(staticValue) # 토큰생성
    print(type(staticValue)) # bytes 이기에 json으로 캐스팅 필요
    test = jwt.decode(staticValue, 'secret key', algorithms='HS256')
    print(test)
    return jsonify({
        'msg':test # {request값 : 'payload'}
    })

app.run(debug=True)