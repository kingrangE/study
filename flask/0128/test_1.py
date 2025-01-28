"""
Flask-login
"""
from flask import Flask
from flask_login import LoginManager,UserMixin
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
db = SQLAlchemy(app)
login_manager = LoginManager() #LoginManager는 로그인 상태 관리를 위한 여러 메서드, 속성 제공

login_manager.init_app(app) #login manager를 현재 app과 연결

"""flask_login을 위한 사용자 정보 담을 클래스"""
class User(UserMixin,db.Model):
    #UseMixin은 Flask-login에서 기본 제공하는 사용자 모델, 로그인 관리에 필요한 메서드를 가짐
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)

@login_manager.user_loader # flask-login에게 user객체 load 방법을 알려주는 것
def load_user(user_id):
    return User.query.get(int(user_id)) #user_id(pk)를 이용하여 get
