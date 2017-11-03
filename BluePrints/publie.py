from flask import Blueprint

blueprint = Blueprint('public',__name__)

@blueprint.route('/')
def home():
    return "blueprint test"

@blueprint.route('/a')
def test():
    print('tste')
    return '성공적'