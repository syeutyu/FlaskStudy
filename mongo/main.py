from mongo.schema import mongoengine
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def post():
 #   id = request.args.get('id')
#    print(id+'들어옴')
    # test = mongoengine(test_num=id)
   # for u in mongoengine.objects():
    #    print('가져오는값')
     #   print(u.test_num)
    u = mongoengine.objects.count()
    print(u)
    for i in range(0,5):
        a = []
        a.append(i)
        print(a)
    print(a)
    #print(u[0]._len_)
    #print(u[0].test_num)
    #print(test)
    return ''

if __name__ =='__main__':
    app.run(debug=True)
