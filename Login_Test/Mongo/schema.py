from mongoengine import *

connect('Login')

class User(Document):
    user_id = StringField(unique=True)
    password = StringField()