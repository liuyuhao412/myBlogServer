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
    return jsonify({'message': '登出成功'}), 200


@bp.route('/protected_content', methods=['GET'])
def protected_content():
    token = request.headers.get('Authorization')
    if token and token.startswith('Bearer '):
        token = token.split(' ')[1]
    if not token:
        return jsonify({'message': '未授权'}), 401
    try:
        decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = decoded_token['user_id']
        # 验证用户身份，返回相应内容
        return jsonify({'message': '这是受保护的内容'})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token 已过期'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': '无效的 Token'}), 401
