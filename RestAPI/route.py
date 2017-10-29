from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"

@app.route('/user/<text>')  # param 값 추출  <int:nun> 이런 형식일 경우 int 값으로 전달 int,float,path 존재
def user(text):
    return helloworld() + "  " + text

@app.route('/data', methods=['POST'])
def getRequest():
    data = request.form['data']
    print(data + " 의 값으로 들어옴")
    return jsonify(data=data, email="syeuty@naver.com"), 207  # return 부분의 뒤에 오는 숫자는 status 코드를 지정
