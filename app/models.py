from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta


class User(db.Model):
    """
    用户模型类，存储用户的基本信息和安全密码。
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,
                         nullable=False, index=True)
    password_hash = db.Column(db.String(512), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """
        使用生成密码哈希的方法来设置用户的密码。
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        验证用户输入的密码是否与存储的哈希密码匹配。
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class UserProfile(db.Model):
    """
    用户资料模型类，存储用户的个人资料信息，包括头像、简介等。
    """
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(
        'User', backref=db.backref('profile', uselist=False))
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    avatar = db.Column(db.String(255), nullable=True)
    info = db.Column(db.Text, nullable=True)
    article_count = db.Column(db.Integer, default=0)
    tag_count = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'username': self.user.username,
            "name": self.name,
            'avatar': self.avatar,
            'email': self.email,
            'info': self.info,
            'articleCount': self.article_count,
            'tagCount': self.tag_count,
        }


class Article(db.Model):
    """
    文章模型类，存储博客文章的标题、描述、内容以及时间戳。
    """
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(
        db.DateTime, default=lambda: datetime.utcnow() + timedelta(hours=8))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(
        'User', backref=db.backref('articles', uselist=False))
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=True)
    category = db.relationship(
        'Category', backref=db.backref('articles', lazy=True))

    def to_dict(self):
        formatted_date = self.date.strftime(
            '%Y-%m-%d %H:%M:%S') if self.date else None

        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "date": formatted_date,
            "name": self.user.profile.name,
        }


class Category(db.Model):
    """
    分类模型类，存储博客文章的分类信息。
    """
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    article_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Category {self.name}>'
