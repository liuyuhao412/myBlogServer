from . import db
from .models import Category

def create_category(name):
    """
    创建新分类并保存到数据库。

    :param name: 分类名称
    :return: 创建的分类对象
    """
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return category

def get_category_by_id(category_id):
    """
    根据分类ID获取分类对象。

    :param category_id: 分类ID
    :return: 分类对象，若不存在则返回 None
    """
    return Category.query.get(category_id)

def update_category(category_id, name=None):
    """
    更新分类信息。

    :param category_id: 分类ID
    :param name: 新名称
    :return: 更新后的分类对象
    """
    category = Category.query.get(category_id)
    if category and name:
        category.name = name
        db.session.commit()
    return category

def delete_category(category_id):
    """
    删除分类。

    :param category_id: 分类ID
    :return: 被删除的分类对象，若不存在则返回 None
    """
    category = Category.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
    return category
