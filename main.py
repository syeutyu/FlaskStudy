from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

def type(date_format):
    def trans(date_str):
        print(date_str)
        print(date_format)
        return datetime.strptime(date_str,date_format)
    print(trans)
    return trans

@app.route('/board',methods=['GET','POST'])
def board():
    print(request.values)
    print(request.values.get("date","2015-03-09",type=type("%Y-%m-%d"))) # 두번째 인자 값은 같을 때만 type 함수가 실행됩니다
    return ' 성공 '

if __name__ == "__main__":  # 해당하는 모듈이 자체적으로 실행되는지 혹은 모듈로 불러올때 분리하기위해 사용
    app.config.PORT = 3000
    app.run(port=app.config.PORT, debug=True)  # debug == True 는 코드를 재시작 해주면 debug 기능도 포함
