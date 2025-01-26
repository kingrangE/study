from flask import Flask,request,url_for

"""
basic , method
"""
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/test/<name>')
def test(name):
    return f'Hello, {name}!'

@app.route('/method',methods=['GET','POST','DELETE','PUT'])
def method():
    if request.method == 'GET':
        return 'GET'
    elif request.method == 'POST':
        return 'POST'
    elif request.method == 'DELETE':
        return 'DELETE'
    elif request.method == 'PUT':
        return 'PUT'

@app.route('/url_test/<name>')
def url_test(name):
    return f'Hello, {name}! 홈으로 : {url_for("hello_world")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)