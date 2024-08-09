from flask import Blueprint

bp = Blueprint('profile', __name__)

@bp.route('/profile', methods=['GET'])
def view_profile():
    # 查看用户个人信息
    pass

@bp.route('/profile', methods=['PUT'])
def update_profile():
    # 更新用户个人信息
    pass
