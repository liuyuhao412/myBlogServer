import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class Config:
    # Flask的配置
    SECRET_KEY = os.getenv('SECRET_KEY') or 'flask:myblog:server:123123123'
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']

    # SQLAlchemy和数据库的配置
    USERNAME = os.getenv('DB_USERNAME')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')
    DATABASE = os.getenv('DB_NAME')
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 动态追踪修改设置，没有设置会有警告
    SQLALCHEMY_ECHO = False  # 查询时显示原始SQL语句
