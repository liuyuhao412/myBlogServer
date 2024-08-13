# Blog博客系统 README

## 项目简介

这是一个使用 Flask 构建的Blog博客系统。

## 环境配置

- 可以参照 requirements.txt 文件里的内容进行安装下载。
- 也可以使用下列命令安装，前提保证你的电脑有可用的python。
```bash
pip install -r requirements.txt
```
## 数据库迁移
使用 Flask-Migrate 进行数据库迁移：
- 初始化数据库
```bash
flask db init
```
- 生成迁移脚本
```bash
flask db migrate -m "迁移的消息提示（自己写）"
```
- 应用迁移
```bash
flask db upgrade
```
## HTTP 状态码及含义
| 状态码                           | 含义                     | 可能的原因                                                       |
|-------------------------------|------------------------|-------------------------------------------------------------|
| **200 OK**                    | 请求成功                   | -                                                           |
| **400 Bad Request**           | 请求无效或格式错误              | - 请求中缺少必要的字段，如用户名或密码。<br>- 提交的密码与确认密码不匹配。<br>- 用户名已存在（注册时）。 |
| **401 Unauthorized**          | 请求未通过身份验证              | -                                                           |
| **500 Internal Server Error** | 服务器在处理请求时发生了错误，无法完成请求。 | - 服务器在处理注册请求时出现意外错误，无法创建用户。                                 |

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

