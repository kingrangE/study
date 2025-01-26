from flask import Flask

"""
type hint
"""
app = Flask(__name__)

@app.route('/')
def index():
    return 'Home'

@app.route('/login/<string:id>/<string:pw>')
def login(id,pw):
    return f'id : {id}, pw : {pw}'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    result = num1 + num2
    return f'덧셈 결과 : {result}'

@app.route('/float/<float:num>')
def test_float(num):
    return f'Float : {float}'

@app.route('/path/<path:subpath>')
def path_test(subpath):
    return f'subpath : {subpath}'

@app.route('/uuid/<uuid:uid>')
def uuid_test(uid):
    return f'uid : {uid}'

if __name__ == "__main__":
    app.run(debug=True)