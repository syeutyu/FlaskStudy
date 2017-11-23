from mongo.schema import testSchema
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def post():
    id = request.args.get('id')
    print(id+'들어옴')
    test = testSchema(test_num=id)
    print(test)
    test.save()
    return '성공'

if __name__ =='__main__':
    app.run(debug=True)
