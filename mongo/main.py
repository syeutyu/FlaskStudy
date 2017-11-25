from mongo.schema import mongoengine
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def post():
    id = request.args.get('id')
    print(id+'들어옴')
    test = mongoengine(test_num=id)
    print(test)
    test.save()
    return ''

if __name__ =='__main__':
    app.run(debug=True)
