from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route('/test')
def testUrl():
    print('testUrl 부분')
    return 'testUrl'


@app.route('/geturl')
def geturl():
    print(url_for('testUrl')) # url_for()의 인자로 들어온 뷰함수의 경로를 찾아 줌
    return redirect(url_for('testUrl'))

app.run(debug=True)