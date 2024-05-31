from flask import Flask
from blueprint.user.user import user_bp
from blueprint.parent.parent import parent_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(parent_bp)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    app.run(debug=True, host='127.0.0.1', port=5000)
