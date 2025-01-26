from flask import Flask,request,jsonify

"""
request (query)
"""
app = Flask(__name__)

@app.route('/')
def index():
    data = request.args
    name = data.get('name')
    age = data.get('age')
    return f'{age}살 {name}님 환영합니다.'

@app.route('/response/<name>',methods=["POST"])
def response(name):
    return jsonify({'message' : f'{name}님 잘 받았습니다.'})


if __name__ == "__main__":
    app.run(debug=True)