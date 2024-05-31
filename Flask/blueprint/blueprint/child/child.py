from flask import Blueprint, url_for


child_bp = Blueprint('child',
                     __name__,
                     url_prefix='/child',
                     template_folder='templates_child',
                     static_folder='static_child',
                     )


@child_bp.route('/')
def index():
    print(url_for('parent.child.index'))
    return '这是子蓝图主页页面'
