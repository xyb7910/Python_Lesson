from datetime import datetime

from blinker import Namespace
from flask import Flask, current_app, url_for, g, render_template, abort, request, template_rendered, \
    got_request_exception

app = Flask(__name__)

# 手动推入应用上下文对象 方式1
app_context_obj = app.app_context()
app_context_obj.push()
print(current_app.name)

# 手动推入应用上下文对象 方式2
with app.app_context():
    print(current_app.name)


@app.route('/')
def index():
    # 应用上下文
    print(current_app.name)
    # 请求上下文
    print(url_for('index'))
    return "Hello World!"


# 在视图函数外获取请求上下文 , 必须手动推入请求上下文
with app.test_request_context():
    print(url_for('index'))


# 使用 g 对象
@app.route('/setuser/<user>/')
def setuser(user: str) -> str:
    g.user = user
    return f"User '{g.user}' was stored in the 'g' object."


@app.route('/getuser/')
def getuser() -> str:
    if hasattr(g, 'user'):
        return f"User retrieved from 'g' object: '{g.user}'"
    else:
        return "No user was set in the 'g' object."


# 钩子函数
def get_current_user():
    return 'CurrentUser'


@app.before_request
def load_user():
    g.user = get_current_user()


@app.route('/test_before/')
def test_before():
    return f"Hello, {g.user}"


@app.teardown_appcontext
def teardown_appcontext(exception):
    return "After request"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/test404/')
def test404():
    abort(404)


@app.context_processor
def inject_user():
    return dict(user_ip=request.remote_addr)


@app.route('/get_user_address/')
def get_user_address():
    return render_template('get_user_address.html')


# 信号机制
# 实现登录信号机制
@app.route('/login_signal/')
def login_signal():
    uname = request.args.get('uname')
    if uname is not None:
        g.uname = uname
        # 发送信号
        login_signal.send()
        return 'Login successful!'
    else:
        return 'Login failed.'


# 创建命名空间
namespace = Namespace()
# 创建登录信号
login_signal = namespace.signal('login')


def login_log(sender):
    uname = g.uname
    now = datetime.now()
    ip = request.remote_addr
    log_data = '{uname} - {ip} - {now}'.format(uname=uname, ip=ip, now=now)
    with open('login_log.txt', 'a') as f:
        f.write(log_data + '\n')
        f.close()


# 监听信号
login_signal.connect(login_log)


# 常见的信号
# template_rendered
def template_rendered_func(sender, template, context):
    print(sender)
    print(template)
    print(context)


template_rendered.connect(template_rendered_func)


# got_request_exception
def request_exception_handler(sender, exception):
    print(exception)
    print(sender)
    print(type(exception))


got_request_exception.connect(request_exception_handler)


@app.route('/division_zero/')
def division_zero():
    a = 1 / 0
    return a


if __name__ == '__main__':
    app.run()
    app.run(debug=True, host='127.0.0.1', port=5000)
