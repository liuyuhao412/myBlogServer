from flask import Blueprint

bp = Blueprint('posts', __name__)

@bp.route('/posts', methods=['GET'])
def list_posts():
    # 显示所有文章
    pass

@bp.route('/posts/<int:id>', methods=['GET'])
def view_post(id):
    # 显示单篇文章
    pass

@bp.route('/posts', methods=['POST'])
def create_post():
    # 创建新文章
    pass

@bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    # 编辑文章
    pass

@bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    # 删除文章
    pass
