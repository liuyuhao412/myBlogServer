from .. import db
from ..models import Article, UserProfile
from datetime import datetime, timedelta


def create_article(user_id, title, content):
    """
    创建新文章并保存到数据库。
    :param title: 文章标题
    :param content: 文章内容
    :return: 创建的文章对象
    """
    article = Article(user_id=user_id, title=title, content=content)
    User = UserProfile.query.filter_by(user_id=user_id).first()
    User.article_count += 1
    db.session.add(article)
    db.session.commit()
    return article


def get_articles(user_id):
    """
    获取所有文章。
    :return: 文章列表
    """
    Articles = Article.query.filter_by(user_id=user_id).all()
    return [{"id": article.id, "title": article.title} for article in Articles]


def get_article_by_id(id):
    """
    根据文章ID获取文章对象。

    :param article_id: 文章ID
    :return: 文章对象，若不存在则返回 None
    """
    article = Article.query.filter_by(id=id).first()
    return article.to_dict() if article else None


def update_article(article_id, title=None, content=None):
    """
    更新文章信息。

    :param article_id: 文章ID
    :param title: 新标题
    :param description: 新描述
    :param content: 新内容
    :return: 更新后的文章对象
    """
    article = Article.query.get(article_id)
    if article:
        if title:
            article.title = title
        if content:
            article.content = content
        article.date = datetime.utcnow() + timedelta(hours=8)
        db.session.commit()
    return article


def delete_article(article_id):
    """
    删除文章。

    :param article_id: 文章ID
    :return: 被删除的文章对象，若不存在则返回 None
    """
    article = Article.query.get(article_id)
    if article:
        User = UserProfile.query.filter_by(user_id=article.user_id).first()
        User.article_count -= 1
        db.session.delete(article)
        db.session.commit()
    return article
