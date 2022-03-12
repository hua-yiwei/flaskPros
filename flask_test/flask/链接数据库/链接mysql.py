"""参考文档 https://www.cnblogs.com/wanggungun/p/14933850.html"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)


class Config:
    """配置参数"""
    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/flask_ex"
    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # # 查询时会显示原始SQL语句
    # SQLALCHEMY_ECHO = True
    # 禁止自动提交数据处理
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False


# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')  # 反推与role关联的多个User模型对象


class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 设置外键


if __name__ == '__main__':
    # # 删除所有表
    # db.drop_all()
    #
    # # 创建所有表
    # db.create_all()
    #
    # # 插入一条角色数据
    # role1 = Role(name='admin')
    # db.session.add(role1)
    # db.session.commit()
    #
    # # 再次插入一条数据
    # role2 = Role(name='user')
    # db.session.add(role2)
    # db.session.commit()
    #
    # # 一次性插入多条数据
    # user1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=role1.id)
    # user2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=role2.id)
    # user3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=role2.id)
    # user4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=role1.id)
    # db.session.add_all([user1, user2, user3, user4])
    # db.session.commit()

    print("-------------------------------查询数据库---------------------------------------")
    print(User.query.filter_by(name='wang').all())
    print(User.query.filter_by(name='wang').all()[0].name)
