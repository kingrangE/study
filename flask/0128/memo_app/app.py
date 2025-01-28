from flask import Flask,render_template,request,redirect,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager,login_user,logout_user,UserMixin,login_required,current_user
load_dotenv()
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    password_hash = db.Column(db.String(512))
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(password,self.password_hash)

class Memo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.String(500),nullable=False)
    
    def __repr__(self):
        return f"<Memo {self.title}>"

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return "MemoApp 소개 페이지입니다."

@app.route("/memos/create",methods=['POST'])
def create_memo():
    title = request.json["title"]
    content = request.json["content"]
    new_memo = Memo(title=title,content = content)
    db.session.add(new_memo)
    db.session.commit()
    return jsonify({'message':f'Memo(title :{title}) Created'})

@app.route("/memos",methods=["GET"])
def list_memos():
    memos = Memo.query.all()
    return jsonify({'id':memo.id, 'title' : memo.title, 'content':memo.content} for memo in memos),200

@app.route("/memos/update/<int:id>",methods=["PUT"])
def update_memo(id):
    memo = Memo.query.get(id)
    if memo : 
        memo.title = request.json["title"]
        memo.content = request.json["content"]
        db.session.commit()
        return jsonify({'message':'Memo was updated'}),200
    else:
        abort(404,description=f"Memo id({id}) cannot find")
    
@app.route('/memos/delete/<int:id>',methods=['DELETE'])
def delete_memo(id):
    memo = Memo.query.get(id)
    if memo : 
        db.session.delete(memo)
        db.session.commit()
        return jsonify({'message':'Memo was deleted'}),200
    else :
        abort(404,description=f"Memo id({id}) cannot find")

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User(username=username,email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        return jsonify({'message':f'{username}님 가입을 축하합니다.'}),201
    return render_template('signup.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and User.check_password(password):
            login_user(user)
            return jsonify({'message':f'{user.username}님 로그인 되었습니다.'})
        return abort(401,description="Invalid Credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return jsonify({'message':'Logged out successfully'}),200