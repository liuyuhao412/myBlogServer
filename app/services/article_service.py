from .. import db
from ..models import Article

def create_article(title, description, content, category_id):
    """
    创建新文章并保存到数据库。

    :param title: 文章标题
    :param description: 文章描述
    :param content: 文章内容
    :param category_id: 分类ID
    :return: 创建的文章对象
    """
    article = Article(title=title, description=description, content=content, category_id=category_id)
    db.session.add(article)
    db.session.commit()
    return article

def get_article_by_id(article_id):
    """
    根据文章ID获取文章对象。

    :param article_id: 文章ID
    :return: 文章对象，若不存在则返回 None
    """
    return Article.query.get(article_id)

def update_article(article_id, title=None, description=None, content=None):
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
        if description:
            article.description = description
        if content:
            article.content = content
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
        db.session.delete(article)
        db.session.commit()
    return article
