from flask import Flask,Blueprint
from test_5 import auth_blueprint
from test_6 import main_blueprint

"""
main file using blueprint modules
"""

app = Flask(__name__)

@app.route('/')
def index():
    return 'original main입니다.'

app.register_blueprint(auth_blueprint,url_prefix="/auth")
app.register_blueprint(main_blueprint,url_prefix="/main")

if __name__ == "__main__":
    app.run(debug=True)