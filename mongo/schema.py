from mongo import *

class testSchema(Document):
    test_num = StringField(default='test')