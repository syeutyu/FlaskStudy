from mongoengine import *

def connection_db(app):
    connect(db=app.config['DB'],host=app.config['HOST'],port=app.config['PORT'])