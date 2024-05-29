from flask import Flask, request, render_template, url_for, redirect, Response, jsonify, views
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


# 类视图

# 定义类视图
class ListView(views.View):
    def dispatch_request(self):
        return '这是定义的一个类视图'


# 注册类视图
app.add_url_rule('/list/', view_func=ListView.as_view('my_list'))

with app.test_request_context():
    print(url_for('my_list'))
if __name__ == '__main__':
    app.run()
    app.run(debug=True, host='127.0.0.1', port=5000)
