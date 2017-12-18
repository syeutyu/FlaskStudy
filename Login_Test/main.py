from Login_Test.config import app

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])