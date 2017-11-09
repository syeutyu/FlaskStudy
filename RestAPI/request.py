from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/data',methods=['GET','POST'])
def getData():
    if request.method == 'GET':
        return request.args["number"]
    else:
        return request.form["number"]


@app.route('/getJson')
def getJson():
     data = request.json
     print(type(data))
     return data

app.run(debug=True)