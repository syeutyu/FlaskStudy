from flask import Flask,request,render_template
from werkzeug  import secure_filename
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('send.html')

@app.route('/form',methods=['POST'])
def save():
    print(request.method) # get 방식으로는 접근이 불가
    f = request.files.get('file')
    f.save('saveFolder/'+f.filename) # 폴더명을 명시하지않을경우 main 폴더 부분에 사진이 생성됩니다
    print(f.filename)
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)