from .. import db
from ..models import UserProfile

def get_user_profile(user_id):
    """
    根据用户ID获取用户资料。

    :param user_id: 用户ID
    :return: 用户资料对象，若不存在则返回 None
    """
    user_profile = UserProfile.query.filter_by(user_id=user_id).first()
    if user_profile is None:
        user_profile = UserProfile(user_id=user_id)
        db.session.add(user_profile)
        db.session.commit()
    data = user_profile.to_dict()
    return data

def update_user_profile(user_id, email=None, avatar=None, info=None):
    """
    更新用户资料。
    :param user_id: 用户ID
    :param email: 用户邮箱
    :param avatar: 新头像URL
    :param info: 新简介
    :return: 更新后的用户资料对象
    """
    profile = UserProfile.query.filter_by(user_id=user_id).first()
    if profile:
        if email:
            profile.email = email
        if avatar:
            profile.avatar = avatar
        if info:
            profile.info = info
        db.session.commit()
    return profile
