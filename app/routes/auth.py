from flask import Blueprint, request, jsonify, current_app
from ..services.user_service import get_user_by_username, create_user
import jwt
import datetime

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400

    user = get_user_by_username(username)
    if user and user.check_password(password):
        # 生成 Token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({
            'token': token,
            'user': {
                'id': user.id,
                'username': username
            },
            'message': '登陆成功'
        }), 200
    else:
        return jsonify({'message': '用户名或密码错误'}), 401


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    if not username or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400

    if password != confirm_password:
        return jsonify({'message': '密码和确认密码不匹配'}), 400

    if get_user_by_username(username):
        return jsonify({'message': '用户名已存在'}), 400

    user = create_user(username=username, password=password)
    if user:
        return jsonify({'message': '注册成功'}), 200
    else:
        return jsonify({'message': '注册失败，请稍后再试'}), 500


@bp.route('/logout', methods=['POST'])
def logout():
    # 处理用户登出
    pass
