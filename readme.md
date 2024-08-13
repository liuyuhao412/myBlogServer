# Blog博客系统的服务器端

## 项目简介

这是一个使用 Flask 构建的Blog博客系统的服务器端，用来和浏览器端进行数据交互。

## 环境配置
### Python环境配置
1. 下载并安装[Python](https://www.python.org/)
2. 安装环境依赖
   - 可以参照 requirements.txt 文件里的内容进行安装下载。
   - 也可以使用如下命令来进行安装
   ```bash
    pip install -r requirements.txt
    ```
### 数据库环境配置
1. 安装并配置[MySQL](https://www.mysql.com/cn/)数据库
2. 进入到config.py文件进行环境配置，我所采用的是.env环境变量，在根目录下创建此文件，并配置相应的参数。


### 数据库迁移
使用 Flask-Migrate 进行数据库迁移，首先在app/models.py中定义所需要的模型，然后使用如下命令：
1. 初始化数据库
```bash
flask db init
```
2. 生成迁移脚本
```bash
flask db migrate -m "迁移的消息提示（自己写）"
```
3. 应用迁移
```bash
flask db upgrade
```
## 项目结构
<pre> 
/server
|-- /app                    # 后端服务器应用
|   |-- /routes                # 存放路由视图的目录
|   |-- /services              # 存放路由视图相关的函数的目录
|   |-- __init__.py            # app应用的初始化文件
|   |-- models.py              # 数据库模型文件
|   |-- utils.py               # 工具包文件
|-- /migration                 # 数据库迁移文件目录
|-- /uploads                   # 上传文件存储目录
|-- .env                       # 环境变量（不上传）
|-- .gitignore                 # Git忽略文件配置
|-- config.py                  # 后端项目配置文件
|-- README.md                  # 项目说明文档
|-- requirements.txt           # 项目依赖文件
|-- run.py                     # 项目运行入口
</pre>

## 运行项目
在本地运行Flask项目
- 设置环境变量
```bash
FLASK_APP=app.py
```
- 启动Flask开发服务器
```bash
flask run
```

## HTTP 状态码及含义
| 状态码                           | 含义                     | 可能的原因                                                       |
|-------------------------------|------------------------|-------------------------------------------------------------|
| **200 OK**                    | 请求成功                   | -                                                           |
| **400 Bad Request**           | 请求无效或格式错误              | - 请求中缺少必要的字段，如用户名或密码。<br>- 提交的密码与确认密码不匹配。<br>- 用户名已存在（注册时）。 |
| **401 Unauthorized**          | 请求未通过身份验证              | -                                                           |
| **500 Internal Server Error** | 服务器在处理请求时发生了错误，无法完成请求。 | - 服务器在处理注册请求时出现意外错误，无法创建用户。                                 |


## 学习资料
- Flask 官方文档： [Flask](https://www.osgeo.cn/flask/)
- Flask-SQLAlchemy 官方文档： [SQLAlchemy](http://www.pythondoc.com/flask-sqlalchemy/)
- Flask-Migrate 官方文档： [Migrate](https://flask-migrate.readthedocs.io/en/latest/)

