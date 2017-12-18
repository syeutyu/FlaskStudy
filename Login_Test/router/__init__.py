from flask_restful import Api
from Login_Test.router.info import *

class routerInjector(object):
    def __init__(self,app):
        self.app = app
        self.setRouter()

    def setRouter(self):
        api = Api(self.app)
        api.add_resource(SignUp,'/create')

