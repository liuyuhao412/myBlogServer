from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config


# 加载环境变量
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # 从配置文件加载配置
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)

    # 启用跨域资源共享
    CORS(app)

    # 导入模型
    from .models import User

    # 注册蓝图或路由
    with app.app_context():
        from .routes import auth
        app.register_blueprint(auth.bp)

    return app
