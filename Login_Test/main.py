from Login_Test.config import app
from Login_Test.Mongo import connection_db

if __name__ == '__main__':
    connection_db(app)
    app.run(debug=app.config['DEBUG'])