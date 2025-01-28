"""
flask, sql을 이용한 로그인 system
"""
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy,session
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = "UserTest"
    uid = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(40),nullable=False,unique=True)
    password = db.Column(db.String(40),nullable=False)
    name = db.Column(db.String(30),nullable=True)

    def __repr__(self):
        return f"User\nuid : {self.uid}\nemail : {self.email}\npassword : {self.password}\nname : {self.name}"

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    users = User.query.all()
    return f"가입된 사용자 목록\n{users}"

@app.route("/signin")
def sign_in():
    data = request.args
    try : 
        email = data["email"]
        password = data["password"]
    except Exception as e :
        return "데이터가 제대로 전달되지 않았습니다."+str(e)


    user = User.query.filter(User.email == email and User.password == password).first() # email, password가 같은 거 가져오기
    if user : #user가 none이 아니라면
        return f"{user.name}님 로그인에 성공하셨습니다."
    else :
        return "email 혹은 password가 일치하지 않습니다."

@app.route("/signup")
def sign_up():
    data = request.args
    try:
        email = data["email"]
        password = data["password"]
    except Exception as e :
        return "데이터가 제대로 전달되지 않았습니다."+str(e)
    try :
        name = data["name"]
    except :
        pass

    try :
        user = User(email=email,password = password,name = name)
    except :
        return "Error when generating user object"
    try :
        db.session.add(user)
        db.session.commit()
    except Exception as e :
        return "Error in db" + str(e)
    return f"{name}님 회원가입 완료되었습니다."

@app.route("/delete_account")
def delete_account():
    data = request.args
    try:
        email = data["email"]
        password = data["password"]
    except Exception as e :
        return "데이터가 제대로 전달되지 않았습니다."+str(e)
    user = User.query.filter(User.email == email and User.password == password).first() # email, password가 같은 거 가져오기
    if not user :
        return "존재하지 않는 email이거나 password가 맞지 않습니다."
    try :        
        db.session.delete(user)
        db.session.commit()
    except Exception as e :
        return "Error in db" + str(e)

    return f"회원 탈퇴가 완료되었습니다."

@app.route("/change_mail")
def change_mail() :
    data = request.args
    try :
        email = data["email"]
        password = data["password"]
        new_email = data["new_email"]
    except Exception as e :
        return "데이터가 제대로 전달되지 않았습니다."+str(e)

    user = User.query.filter(User.email == email and User.password == password).first() # email, password가 같은 거 가져오기
    if not user :
        return "존재하지 않는 email이거나 password가 맞지 않습니다."
    user.email = new_email
    db.session.commit()
    return f"{new_email}로 변경이 완료 되었습니다."

if __name__ == "__main__":
    app.run(debug=True)