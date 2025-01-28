from flask import Flask,request,redirect,url_for,session
from flask_login import LoginManager,UserMixin,login_required,login_user,logout_user,current_user
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
"""
session으로 사용자 로그인 정보를 관리하는 파일
"""
load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
db = SQLAlchemy(app)
login_manager = LoginManager() #LoginManager는 로그인 상태 관리를 위한 여러 메서드, 속성 제공
login_manager.init_app(app)
login_manager.login_view = 'login' #login_required에 접근하는데 login하지 않은 상태라면 해당 이름의 method로 이동

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return f'User_id : {self.id} / User_name : {self.user_name} '

with app.app_context() :
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    user_id = session.get('user_id')
    if user_id : 
        user = User.query.get(user_id)
        login_user(user)
        return redirect(url_for('protected'))
    users = User.query.all()
    return f'로그인되지 않았습니다.\n가입한 사용자 목록\n{users}'

@app.route('/protected')
@login_required #로그인 필요하게 강제 (로그인 하지 않은 상태로 접근 시, login_manager에 등록한 view로 이동)
def protected():
    return f'Logged in as {current_user.user_name}'

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        user_name = request.form["user_name"]
        password = request.form["password"]
        user = User.query.filter_by(user_name =user_name).first()
        if user and user.password ==password :
            session['user_id'] = user.id
            login_user(user)
            return redirect(url_for('protected'))
        
    return '''
        <form method="POST">
            Username : <input type="text" name="user_name"><br/>
            Password : <input type="text" name="password"><br/>
            <input type="submit" value="LogIn">
        </form>
    '''

@app.route('/logout')
def logout():
    logout_user()
    session.pop('user_id',None)
    return redirect(url_for('index'))

@app.route('/signup')
def signup():
    data = request.args
    user_name = data["user_name"]
    password = data["password"]
    test_user = User(user_name= user_name,password=password)
    db.session.add(test_user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)