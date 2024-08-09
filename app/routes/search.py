from flask import Blueprint, request, jsonify

bp = Blueprint('search', __name__)

@bp.route('/search', methods=['GET'])
def search():
    # 搜索文章
    pass
