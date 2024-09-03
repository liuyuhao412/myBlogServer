from flask import Blueprint, request, current_app, jsonify
import jwt
from ..services.article_service import create_article, get_articles, get_article_by_id, update_article, delete_article

bp = Blueprint('posts', __name__)


@bp.route('/articles', methods=['GET'])
def list_posts():
    token = request.headers.get('Authorization')
    if token:
        token = token.split(' ')[1]
        decoded_token = jwt.decode(
            token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = decoded_token['user_id']
    else:
        user_id = None
    articles = get_articles(user_id)
    return jsonify({'message': '获取文章列表成功', 'data': articles}), 200


@bp.route('/articles/<int:id>', methods=['GET'])
def view_post(id):
    article = get_article_by_id(id)
    return jsonify({'message': '获取文章成功', 'data': article}), 200


@bp.route('/articles', methods=['POST'])
def create_post():
    token = request.headers.get('Authorization')
    token = token.split(' ')[1]
    decoded_token = jwt.decode(
        token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    user_id = decoded_token['user_id']
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    create_article(user_id, title, content)

    return jsonify({'message': '发布文章成功'}), 200


@bp.route('/articles/<int:id>', methods=['PUT'])
def update_post(id):
    article = get_article_by_id(id)
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    update_article(id, title, content)
    return jsonify({'message': '文章编辑成功'}), 200


@bp.route('/articles/<int:id>', methods=['DELETE'])
def delete_post(id):
    delete_article(id)
    return jsonify({'message': '文章删除成功'}), 200
