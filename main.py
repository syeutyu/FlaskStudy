from flask import Flask, request, abort
from datetime import datetime
from flask.views import View
app = Flask(__name__)

# def type(date_format):
#     def trans(date_str):
#         print(date_str)
#         print(date_format)
#         return datetime.strptime(date_str,date_format)
#     print(trans)
#     return trans
#
# @app.route('/board',methods=['GET','POST'])
# def board():
#     print(request.values)
#     print(request.values.get("date","2015-03-09",type=type("%Y-%m-%d"))) # 두번째 인자 값은 같을 때만 type 함수가 실행됩니다
#     return ' 성공 '
class ShowUser(View):


    def decorator(*args, **kwargs): # 1번째 인자 값은 튜블의 수를 모를때 2번째 인자 값은 딕셔너리 형식의 수를 모를때
        print('send401')
        abort(401)
    # def dispatch_request(self): # 요청이 들어오면 무조건 이 메소드를 실행
    #     print("들어옴")
    #     return "들어옴"

    def prints(self):
        print('print')

app.add_url_rule('/users/',view_func=ShowUser.as_view('show'),methods=['GET']) # as_view 뷰함수로 클래스를 기반으로 한 플러그 뷰로 객체생성을 담당
if __name__ == "__main__":  # 해당하는 모듈이 자체적으로 실행되는지 혹은 모듈로 불러올때 분리하기위해 사용
    app.config.PORT = 3000
    app.run(port=app.config.PORT, debug=True)  # debug == True 는 코드를 재시작 해주면 debug 기능도 포함
