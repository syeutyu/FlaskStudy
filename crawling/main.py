from flask import Flask
from crawling.router import router

app  = Flask(__name__)

if __name__ == '__main__':
    router(app)
    app.run(debug=True)
