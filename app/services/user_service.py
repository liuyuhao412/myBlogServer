from .. import db
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash

def get_user_by_username(username):
    """
    根据用户名获取用户对象。

    :param username: 用户名
    :return: 用户对象，若不存在则返回 None
    """
    return User.query.filter_by(username=username).first()

def create_user(username, password):
    """
    创建新用户并保存到数据库。

    :param username: 用户名
    :param password: 用户密码
    :param email: 用户邮箱
    :return: 创建的用户对象
    """
    user = User(username=username)
    user.set_password(password)  # 设置密码哈希
    db.session.add(user)  # 添加到会话
    db.session.commit()  # 提交到数据库
    return user



def get_user_by_id(user_id):
    """
    根据用户ID获取用户对象。

    :param user_id: 用户ID
    :return: 用户对象，若不存在则返回 None
    """
    return User.query.get(user_id)

def update_user_email(user_id, new_email):
    """
    更新用户的邮箱地址。

    :param user_id: 用户ID
    :param new_email: 新邮箱地址
    :return: 更新后的用户对象
    """
    user = User.query.get(user_id)
    if user:
        user.email = new_email
        db.session.commit()
    return user

def delete_user(user_id):
    """
    删除用户。

    :param user_id: 用户ID
    :return: 被删除的用户对象，若不存在则返回 None
    """
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user
