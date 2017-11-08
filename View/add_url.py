from flask import Flask, request
from View.testClass import testClass
app = Flask(__name__)

# Pluggable View란 각각의 url에따라 보여줘야 되는 페이지가 많아지는 단점을 예방하기 위해서 생성됨
# main에서는 add_url_rule로 class를 불러주고

testC = testClass.as_view('testClass',templateName='init.html')

def test():
    return 'test문법 입니다'

app.add_url_rule('/init/','endpoint',test) # add_url_rule 메소드는 @app.route 데코레이션이 필요없이 간단하게 정의가 가능
app.add_url_rule('/class/',view_func=testC)

app.run(debug=True)