from datetime import datetime

from flask import Flask, request, render_template, url_for, redirect, Response, jsonify, views
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


# 使用template模版返回单一数据
@app.route("/test/template/")
def template():
    return render_template('index.html', username='ypb', email='1502.@qqcom')


# 使用template模版返回多个数据
def templates():
    content = {
        'username': 'ypb',
        'password': '12>ddwsd',
        'email': '1502.@qqcom',
        'description': '对象是一个二哈',
    }
    return render_template('/mutil/index.html', **content)


app.add_url_rule('/test/templates/', endpoint='my_templates', view_func=templates)


# 在模版中url_for
@app.route('/test/url_for/', endpoint='prepare')
def url_for():
    return render_template('/url_for/index.html/')


@app.route('/test/url_for/login/', endpoint='login')
def url_for_login():
    # return '这是登录界面'
    return render_template('/url_for/login.html/')


@app.post('/test/url_for/loginsuc/', endpoint='loginsuc')
def url_for_loginsuc():
    message = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
    }
    return '登录成功，获取到的用户名为 %s，获取到的用户的密码为 %s' % (message['username'], message['password'])


@app.route('/test/url_for/register/', endpoint='register')
def url_for_register():
    return '骗你呢，这个这个注册是玩呢🤣🤣'


# 过滤器的使用
@app.route('/test/filter/')
def test_filter():
    content = {
        "name": "ypb",
        "age": -18,
        "desc": "我是i人",
        "message": "aaddeadedadadcea",
        "articles": ['go', 'java', 'python', 'c', 'javascript'],
        "grade": 19
    }
    return render_template('/filter/index.html', **content)


# 自定义转换过滤器
@app.template_filter('cut_ut')
def cut_ut(text):
    return text.replace('a', '哈哈哈哈')


# 自定义时间过滤器
@app.template_filter('time_filter')
def time_filter(time):
    if isinstance(time, datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return '刚刚'
        elif 60 < timestamp < 3600:
            minutes = timestamp / 60
            return '%s 分钟之前' % int(minutes)
        elif 3600 < timestamp < 86400:
            hours = timestamp / 3600
            return '%s 小时之前' % int(hours)
        elif 86400 < timestamp < 86400 * 30:
            days = timestamp / 86400
            return '%s 天之前' % int(days)
        else:
            return time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return time


if __name__ == '__main__':
    app.run()
    app.run(debug=True, host='127.0.0.1', port=5000)
