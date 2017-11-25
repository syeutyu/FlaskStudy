from mongo import *

class mongoengine(Document):
    test_num = StringField(default='test')