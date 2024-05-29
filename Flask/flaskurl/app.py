from flask import Flask, request, render_template, url_for, redirect, Response, jsonify
from werkzeug.routing import BaseConverter

# import config
app = Flask(__name__)
# app.debug = True
# app.config.update(DEBUG=True)
# app.config.from_object(config)
app.config.from_pyfile("config.py")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 路径参数 为 int
@app.route('/article/<int:id>/')  # 指定参数数据类型为字符串 支持string int float path uuid any,默认为string
def list(id):
    # 输出文章id
    print(id)
    return '你请求的文章详情id为：%s' % id


# 路径参数为 any
@app.route('/<any(user, blog):module>/<int:id>/')
def article(module, id):
    return '你请求的模块为%s，对应的id为%d' % (module, id)


# 请求参数
@app.route('/getuser/', methods=['GET', 'POST'])
def getuser():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return 'POST方式接收到的参数的用户名为%s， 接收到的参数的密码为%s' % (username, password)


# URL 匹配 视图函数 构造路由
@app.route("/chanurl/")
def changeUrl():
    # 使用 url_for 准备动态路由，第一个参数为视图函数名称，多余的参数会作为url的查询参数
    return url_for("changedUrl2", id=16, num=20)


@app.route("/changedurl/")
def changedUrl1():
    return "这是修改定向后的url"


@app.route("/changedurl2/<int:id>/")
def changedUrl2():
    return "这是修改定向后的url2,获取的id值为%d" % id


# 自定义类型转换器
'''
1. 实现一个类，继承自 `BaseConverter`
2. 在自定义的类中，重写 `regex`, 也就是这个变量的正则表达式
3. 将自定义的类，映射到 `app.url_map.converters` 上。 理解为加入到字典 DEFAULT_CONVERTERS 中
'''


class TelephoneConverter(BaseConverter):
    regex = r'\+?1?\d{9,15}$'
    '''
    \+?：匹配电话号码可能以的加号开始，加号前面的?表示加号出现0次或1次。
    1?：匹配电话号码可能以的1开始，1前面的?表示1出现0次或1次。这在一些地方用于表示国际电话区号的开始。
    \d{9,15}：匹配一个长度在9到15之间的数字字符串，表示电话号码的主体部分。
    $：表示字符串的结束。
    '''


app.url_map.converters['tel'] = TelephoneConverter


@app.route('/test/<tel:telphone>/')
def check_telphone(telphone):
    return '你输入的电话号码为 %s ' % telphone


# 查询多个模块参数 -- 传统做法
@app.route('/test/<modules>/')
def query_modules(modules):
    print(modules)
    lm = modules.split('+')
    return '你要查询的模块为%s' % lm


# 查询多个模块参数 -- 重写 to_python 方法
class handleModules(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    # 重写 to_url 方法
    def to_url(self, value):
        return '+'.join(value)


app.url_map.converters['handleModules'] = handleModules


@app.route('/to_python/<handleModules:modules>/')
def check_handleModules(modules):
    print(modules)
    return '你要查询的模块是%s' % modules


@app.route('/to_url/')
# 返回一个 url
def test_to_url():
    args = url_for('check_handleModules', modules=['host', 'test'])
    return '构造出来的url为 %s' % args


# 重定向

# 登录界面
@app.route('/login/')
def login():
    return "这是登录界面"


# 用户主页面
@app.route('/profile/')
def profile():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        return redirect(url_for('login'))
    else:
        return "这是用户主页面"


# 自定义 Response 实现向客户端发送 JSON数据
'''
1. 继承 `Response` 类
2. 实现方法 `force_type(cls, rv, environ=None)`
3. 指定 `app.response_class` 为自定义的 `Response` 对象
'''

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
    # 修改host
    app.run(debug=True, host='127.0.0.1', port=5000)
