from flask import Blueprint

bp = Blueprint('tags', __name__)

@bp.route('/tags', methods=['GET'])
def list_tags():
    # 显示所有标签
    pass

@bp.route('/tags', methods=['POST'])
def create_tag():
    # 创建新标签
    pass

@bp.route('/tags/<int:id>', methods=['PUT'])
def update_tag(id):
    # 编辑标签
    pass

@bp.route('/tags/<int:id>', methods=['DELETE'])
def delete_tag(id):
    # 删除标签
    pass
