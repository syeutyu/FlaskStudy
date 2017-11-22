from flask import Flask
#from BluePrints import publie

app = Flask(__name__)

#
#app.register_blueprint(publie.blueprint, url_prefix='/test')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

# loalhost:5000/test/ 뒤의 blueprint에 적용한 route에 따라서 url 매칭 가능