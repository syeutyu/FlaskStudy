from mongo import *

class User(Document):
    id = StringField(required=True,unique=True)
    password = StringField(required=True,unique=True)