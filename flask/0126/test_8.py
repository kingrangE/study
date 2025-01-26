from flask import Flask,session,request

app = Flask(__name__)

app.secret_key='asdf'

@app.route('/')
def index():
    name = session.get('name')
    if name :
        return f'{name}님 환영합니다.'
    else :
        return '로그인을 해주세요.'
    
@app.route('/login')
def login():
    name = request.args.get('name')
    session['name']=name
    return f'{name}님 로그인 완료되었습니다.'
@app.route('/logout')
def logout():
    session.clear()
    return '로그아웃이 완료되었습니다.'

if __name__ == "__main__":
    app.run(debug=True)