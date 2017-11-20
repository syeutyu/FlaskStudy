from flask import Flask,request,jsonify
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

@app.route("/datasend/",methods=["GET"])
def androidTest():
    a = request.args["data"]
    print("들어온값 %d",a)
    return jsonify({'s':'1000'})

app.run(host='0.0.0.0')