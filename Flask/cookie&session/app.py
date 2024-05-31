import os
from datetime import timedelta

from flask import Flask, request, Response, make_response, session, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


# 设置 cookie
# @app.get('/login/<string:name>/<string:password>/')
# def login(name, password):
#     resp = Response('Welcome {}'.format(name))
#     resp.set_cookie('name', name)
#     resp.set_cookie('password', password)
#     return resp


# 获取 cookie
@app.get('/getinfo/')
def getInfo():
    resp = Response('Welcome {}'.format(request.cookies.get('name')))
    return resp


# 删除 cookie
@app.get('/delete_cookie/')
def delete_cookie():
    resp = make_response('Delete Cookie')
    resp.delete_cookie('name')
    resp.delete_cookie('password')
    return Response('Delete Cookie User')


# 设置过期时间


# 设置 session

# 生成密钥
app.config['SECRET_KEY'] = os.urandom(24)
# 设置过期时间
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# 设置 session
# @app.route('/')
# def index():
#     session['username'] = "admin"
#     session['password'] = "123456"
#     # 底层实现
#     # resp = Response()
#     # resp.set_cookie('session')
#     # 设置 session 的过期时间
#     session.permanent = True
#     return Response('Set Session Successfully')


# 获取 session
@app.route('/get_session/')
def get_session():
    username = session.get('username')
    password = session.get('password')
    print(username)
    print(password)
    return Response('Get Session Successfully')


# 删除 session
@app.route('/delete_session/')
def delete_session():
    # 删除指定 key session
    session.pop('username')
    session.pop('password')
    # 删除全部的 session
    session.clear()
    return Response('Delete Session Successfully')


# 使用 session 登录注册功能
@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        try:
            return render_template('login.html')
        except TemplateNotFound:
            return "Template not found"
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if session.get(username) == password:
            print('Logged in successfully')
            return render_template('index.html')
        else:
            return 'Incorrect username or password'


@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session[username] = password
        return 'Registered successfully'
    if request.method == 'GET':
        return render_template('register.html')


@app.route("/index/")
def index():
    return '这是系统主页面'


@app.route('/logout/')
def logout():
    session.clear()
    return 'Logged out successfully'


if __name__ == '__main__':
    app.run()
    app.run(debug=True, host='127.0.0.1', port=5000)
