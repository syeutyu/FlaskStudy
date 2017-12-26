from flask import Flask,request,render_template
from werkzeug  import secure_filename
import os
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('send.html')

@app.route('/form',methods=['POST'])
def save():
    print(request.method) # get 방식으로는 접근이 불가
    f = request.files.get('file')
    f.save(os.path.dirname(os.path.abspath(__file__))+'\\saveFolder\\'+f.filename) # 폴더명을 명시하지않을경우 main 폴더 부분에 사진이 생성됩니다
    os.remove(os.path.dirname(os.path.abspath(__file__))+'\\saveFolder\\'+f.filename) # 파일 삭제
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)