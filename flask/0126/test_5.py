from flask import Flask,Blueprint

"""
blueprint test1
"""

auth_blueprint = Blueprint('/auth',__name__)

@auth_blueprint.route('/login')
def login():
    return 'login'
@auth_blueprint.route('/logout')
def logout():
    return 'logout'

app = Flask(__name__)

# app.register_blueprint(auth_blueprint,url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)