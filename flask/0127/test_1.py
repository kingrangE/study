"""
MySQL 연동
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy,session
from sqlalchemy import func
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
db = SQLAlchemy(app) # SQLAlchemy 객체 생성
class User(db.Model):
    #아래와 같이 테이블 이름 직접 지정하지 않으면, class명의 소문자(user)로 설정됩니다.
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)

    def __repr__(self):# 객체의 문자열 표현 (객체 출력시 해당 문자열이 출력)
        return '<User %r>' % self.user_name

with app.app_context():
    db.create_all() # model에 정의된 테이블 생성

    #create
    new_user = User(user_name = "길원",email="test@qwer.com") #user 모델 인스턴스 생성
    db.session.add(new_user) # 사용자 DB session에 추가
    db.session.commit() # DB에 실제 반영
    print("All create success")
    #read
    user = User.query.filter_by(user_name="길원").first() # user_name = 길원인 첫번쨰 record get (없으면 None)
    users = User.query.all() # User 모든 record get
    user = db.session.get(User,1) # id(pk)를 알고 있다면 해당 key로 가져올 수 있음
    print("All reads success")
    """filter 추가 예시 (filter -> 복잡 조건, filter_by -> 간단 조건)"""
    users = User.query.filter(User.email.endswith('@qwer.com')).all() # email이 @qwer.com으로 끝나는 모든 record get
    """%, _를 이용한 복잡한 조건"""
    users = User.query.filter(User.email.like("%qwer%")).all() # email이 qwer을 중심으로 앞 뒤에 하나 이상의 문자열이 오는 record get
    users = User.query.filter(User.email.ilike("%QWER%")).all() # like와 동일하나 대소문자 구분 X
    """limit 예시"""
    users = User.query.limit(5).all() # User의 처음 5개 record만
    """offset 예시 ( 초반 몇 개 무시 )"""
    users = User.query.offset(4).all() # User의 처음 4개 record 무시하고 나머지 전부
    """오름차순 정렬"""
    users = User.query.order_by(User.user_name).all() # User의 모든 record를 user_name 기준 오름차순 정렬하여 get
    """개수 세기"""
    count_of_user = User.query.filter_by(user_name="길원").count() # user_name = 길원 인 record 개수 반환
    print("count of column user_name equals 길원",count_of_user)
    """func 모듈"""
    users = User.query.filter(func.lower(User.email)=="test@qwer.com").all()

    #update
    """1. for문 이용"""
    users = User.query.filter_by(email = "test@qwer.com").all()
    for user in users:
        if (user.user_name == "길원"): #이름이 길원이면
            user.email = "tset@qwer.com" #이메일 변경
    db.session.commit() #commit을 이용하여 db에 반영
    """2. update 이용"""
    User.query.filter_by(email="tset@qewr.com").update({'email':'qwer@test.com'})
    db.session.commit() #update 사용 시, 즉시 db에 반영되므로 commit 필요 없음
    print("All update success")
    #delete
    user = User.query.filter_by(user_name = "길원").first()
    db.session.delete(user)
    db.session.commit()
    print("All delete success")