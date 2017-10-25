from flask import  Flask,request
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"

@app.route('/user/<text>') # param 값 추출  <int:nun> 이런 형식일 경우 int 값으로 전달 int,float,path 존재
def user(text):
    return helloworld()+"  " +text

@app.route('/data',methods=['POST'])
def getRequest():
    data = request.form['data']
    print(data+" 의 값으로 들어옴")
    return "데이터 들어옴",207 # return 부분의 뒤에 오는 숫자는 status 코드를 지정
if __name__ =="__main__": # 해당하는 모듈이 자체적으로 실행되는지 혹은 모듈로 불러올때 분리하기위해 사용
    app.run(port=3000, debug = True) # debug == True 는 코드를 재시작 해주면 debug 기능도 포함