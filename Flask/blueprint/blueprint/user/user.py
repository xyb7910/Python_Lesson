from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

user_bp = Blueprint('user',
                    __name__,
                    url_prefix='/user',
                    static_folder='static_user',
                    template_folder='templates_user'
                    )


@user_bp.route('/')
def index():
    return '这是用户主页面'


@user_bp.route('/login/')
def login():
    try:
        return render_template('/login.html')
    except TemplateNotFound:
        return 'template not found'

