from flask import Flask,Blueprint

"""
blueprint module
"""

main_blueprint = Blueprint('main',__name__)

@main_blueprint.route('/home')
def home():
    return 'main의 home 화면입니다.'