from mongoengine import *

def connection_db(app):
    connect(db='login',host='localhost',port=27017)