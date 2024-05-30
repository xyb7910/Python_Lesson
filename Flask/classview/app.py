import functools
from datetime import datetime

from flask import Flask, request, render_template, url_for, redirect, Response, jsonify, views, typing as ft
from flask.views import View, MethodView
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


class JSONResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            # 是字典类型在进行操作
            res = jsonify(rv)
        else:
            # 如果不是字典类型，我们可以直接使用rv
            res = rv
        return super(JSONResponse, cls).force_type(res, environ)


app.response_class = JSONResponse


@app.route('/send_json/')
def send_json():
    return {'username': request.args.get('username'), 'password': request.args.get('password')}


# add_url_rule 与 route 的等价写法
@app.route('/test_add_url_rule/')
def test_add_url_rule():
    return "这是测试 `add_url_rule()`"


def test_add_url_rule2():
    return "这是测试 `add_url_rule()`"


app.add_url_rule("/add_url_rule/", endpoint='aur', view_func=test_add_url_rule2)


# 类视图的学习
class User:
    pass


class Story:
    pass


class UserList(View):
    def dispatch_request(self):
        user = User.query.all()
        return render_template('user.html', object=user)


class ListView(View):
    # 定义一个类接收 模型model 和 模板template
    def __int__(self, model, template):
        self.model = model
        self.template = template

    def dispatch_request(self):
        items = self.model.query.all()
        return render_template(self.template, object=items)


# 创建视图
app.add_url_rule(
    '/users/',
    view_func=ListView.as_view('user_list', User, 'user_list.html'),
)

app.add_url_rule(
    '/stories/',
    view_func=ListView.as_view('story_list', Story, 'story_list.html'),
)


# 传递 url 变量
class DetailView(View):
    def __init__(self, model):
        self.model = model
        self.template = f'{model.__name__.lower()}/detail.html'

    def dispatch_request(self, id):
        item = self.model.query.get_or_404(id)
        return render_template(self.template, object=item)


app.add_url_rule(
    '/users/<int:id>/',
    view_func=DetailView.as_view('user_detail', User)
)


# 方法视图
class LoginView(MethodView):
    # 将渲染模板函数抽离
    def __dump(self, error_message=None):
        return render_template('method_view/index.html', error_message=error_message)

    # get methods
    def get(self, error_message=None):
        return self.__dump(error_message)

    # post methods
    def post(self):
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return render_template('method_view/admin_index.html')
        else:
            # return self.get(error_message='傻der，用户名或者密码输错啦！')
            return self.__dump(error_message='傻der，用户名或者密码输错啦！')


# 注册视图
app.add_url_rule('/login/', endpoint='login', view_func=LoginView.as_view('login'))

# 自定义装饰器
# 模拟cookie
cookie = {'username': None, 'password': None, 'repassword': None}
is_logged_in = False


@app.route('/check_logged_in/<string:username>/<string:password>/<string:repassword>/')
def is_user_logged_in(username, password, repassword):
    if username and password and password == repassword:
        cookie['username'] = username
        cookie['password'] = password
        cookie['repassword'] = repassword
        is_logged_in = True
        return "True"
    else:
        return "False"


def login_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        # 假设我们有一个函数is_user_logged_in()，它会检查用户是否登录
        # 如果用户未登录，我们将返回一个错误消息
        print(is_logged_in)
        if not is_logged_in:
            return "Please log in first."
        # 如果用户已经登录，我们将调用原始函数
        return f(*args, **kwargs)

    return decorated_function


@app.route('/say_hello/')
@login_required
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
    app.run(debug=True, host='127.0.0.1', port=5000)
