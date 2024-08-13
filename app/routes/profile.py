from flask import Blueprint, request, jsonify, current_app, send_from_directory
from ..services.user_profile_service import get_user_profile, update_user_profile
from werkzeug.utils import secure_filename
import jwt
import os

bp = Blueprint('profile', __name__)
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@bp.route('/get_user_profile', methods=['GET'])
def view_profile():
    token = request.headers.get('Authorization')
    if token and token.startswith('Bearer '):
        token = token.split(' ')[1]
        decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = decoded_token['user_id']
        data = get_user_profile(user_id)
        return jsonify({'message': '获取用户成功', 'data': data})
    else:
        return jsonify({'message': '用户资料未找到'}), 404

@bp.route('/upload-avatar', methods=['POST'])
def upload_avatar():
    if 'file' not in request.files:
        return jsonify({'error': '没有文件部分'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = 'uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        return jsonify({'avatarUrl': f'/uploads/{filename}'}), 200

    return jsonify({'error': '不允许的文件类型'}), 400

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_file_dir)
    parent_dir = os.path.dirname(parent_dir)
    uploads_dir = os.path.join(parent_dir, 'uploads')
    return send_from_directory(uploads_dir, filename)

@bp.route('/update_profile', methods=['POST'])
def update_profile():
    token = request.headers.get('Authorization')
    token = token.split(' ')[1]
    decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    user_id = decoded_token['user_id']

    data = request.get_json()
    email = data.get('email')
    avatar = data.get('avatar')
    info = data.get('info')
    profile = update_user_profile(user_id, email, avatar, info)
    return jsonify({'message': '个人信息更新成功'}), 200

