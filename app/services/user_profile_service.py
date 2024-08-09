from .. import db
from ..models import UserProfile

def create_user_profile(user_id, avatar=None, info=None):
    """
    创建用户资料。

    :param user_id: 用户ID
    :param avatar: 用户头像URL
    :param info: 用户简介
    :return: 创建的用户资料对象
    """
    profile = UserProfile(user_id=user_id, avatar=avatar, info=info)
    db.session.add(profile)
    db.session.commit()
    return profile

def get_user_profile(user_id):
    """
    根据用户ID获取用户资料。

    :param user_id: 用户ID
    :return: 用户资料对象，若不存在则返回 None
    """
    return UserProfile.query.filter_by(user_id=user_id).first()

def update_user_profile(user_id, avatar=None, info=None):
    """
    更新用户资料。

    :param user_id: 用户ID
    :param avatar: 新头像URL
    :param info: 新简介
    :return: 更新后的用户资料对象
    """
    profile = UserProfile.query.filter_by(user_id=user_id).first()
    if profile:
        if avatar:
            profile.avatar = avatar
        if info:
            profile.info = info
        db.session.commit()
    return profile

def delete_user_profile(user_id):
    """
    删除用户资料。

    :param user_id: 用户ID
    :return: 被删除的用户资料对象，若不存在则返回 None
    """
    profile = UserProfile.query.filter_by(user_id=user_id).first()
    if profile:
        db.session.delete(profile)
        db.session.commit()
    return profile
