from flask import Blueprint, url_for
from blueprint.child.child import child_bp

parent_bp = Blueprint('parent',
                      __name__,
                      url_prefix='/parent',
                      static_folder='static_parent',
                      template_folder='templates_parent'
                      )

# 蓝图的嵌套定义
parent_bp.register_blueprint(child_bp)


@parent_bp.route('/')
def index():
    return '这是父蓝图主页页面'
