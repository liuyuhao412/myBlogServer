from flask import Blueprint

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    # 处理用户注册
    pass

@bp.route('/login', methods=['POST'])
def login():
    # 处理用户登录
    pass

@bp.route('/logout', methods=['POST'])
def logout():
    # 处理用户登出
    pass
