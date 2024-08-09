from flask import Blueprint

bp = Blueprint('comments', __name__)

@bp.route('/posts/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    # 添加评论
    pass

@bp.route('/posts/<int:post_id>/comments', methods=['GET'])
def list_comments(post_id):
    # 查看评论
    pass

@bp.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    # 删除评论
    pass
