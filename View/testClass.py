from flask import render_template
from flask.views import MethodView

class testClass(MethodView):
    templateName = None

    def __init__(self,templateName):
        self.templateName = templateName

    def get(self):
        return render_template(self.templateName)