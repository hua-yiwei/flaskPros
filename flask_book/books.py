"""
2. 添加书和作者模型
    a. 模型继承 db.Model
    b. __tablename__ 表名
    c. db.Column 字段
    d. db.relationship 引用关系
3. 添加数据
4. 使用模板显示数据库查询信息
    a. 查询所有的作者信息，让信息传递给模板
    b. 模板中按照格式，依次for循环作者和书籍即可（作者获取书籍，用的是关系引用）
5. 使用WTF表单
    a. 自定义表单类
    b. 模板中显示
    c. secret_key / 编码格式 / csrf_token
6. 实现相关的增删改查
    a. 添加数据
    b. 删除数据->网页上删除->发送删除的书籍（作者）id给指定路由->路由接收参数
"""
# -*- coding:utf-8 -*-
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pymysql

# import sys
# reload(sys)


pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/flask_books"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "itheima"

db = SQLAlchemy(app=app)


# 创建数据库模型类
# 创建作者类
class Author(db.Model):
    # 表名
    __tablename__ = "authors"
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 关系引用
    # books是给自己用的（Author）模型类，author是给Book模型用的
    books = db.relationship("Book", backref="author")

    def __repr__(self):
        return "Author:{}".format(self.name)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))

    def __repr__(self):
        return "Author:{} {}".format(self.name, self.author_id)


# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField("作者", validators=[DataRequired()])
    book = StringField("书籍", validators=[DataRequired()])
    submit = SubmitField("提交")


# 删除作者
@app.route("/delete_author/<author_id>")
def delete_author(author_id):
    # 1. 查询数据库，是否有该id的作者
    author = Author.query.get(author_id)
    if author:  # 2. 如果有就删除(先删除书，再删除作者)
        try:
            Book.query.filter_by(author_id=author.id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            flash(f"删除作者出错{e}")
            db.session.rollback()
    else:
        flash("没有该作者")
    return redirect(url_for("index"))


# 删除书籍
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    # 1. 查询数据库，是否有该id的书
    book = Book.query.get(book_id)
    # 2. 如果有就删除
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            flash(f"删除书籍出错{e}")
            db.session.rollback()
    else:
        print("没有该书籍")
    return redirect(url_for("index"))


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建自定义表单类
    author_form = AuthorForm()
    """
    验证逻辑：
    1. 调用WTF的函数实现验证
    2. 验证通过，获取数据
    3. 判断作者是否存在
    4. 如果作者存在，判断书籍是否存在，没有重复书籍就添加，有就提示
    5. 如果作者不存在，就添加作者和书籍
    6. 验证不通过，提示错误
    """
    if request.method == "POST":
        # 1. 调用WTF的函数实现验证
        if author_form.validate_on_submit():  # 验证通过
            # 2. 验证通过，获取数据
            author_name = author_form.author.data
            book_name = author_form.book.data
            # 3. 判断作者是否存在
            author = Author.query.filter_by(name=author_name).first()
            if author:  # 4. 如果作者存在
                # 判断书籍是否存在
                book = Book.query.filter_by(name=book_name).first()
                if book:
                    flash("已经存在同名书籍")
                # 没有重复书籍就添加
                else:
                    try:
                        new_book = Book(name=book_name, author_id=author.id)
                        db.session.add(new_book)
                        db.session.commit()
                    except Exception as e:
                        flash("添加数据错误，错误为{}".format(e))
                        db.session.rollback()
            else:  # 5. 如果作者不存在
                try:
                    new_author = Author(name=author_name)
                    db.session.add(new_author)
                    db.session.commit()
                    new_book = Book(name=book_name, author_id=new_author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    flash("添加数据错误，错误为{}".format(e))
                    db.session.rollback()

        else:  # 验证不通过
            flash("参数不全")

    authors = Author.query.all()
    return render_template("books.html", authors=authors, form=author_form)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # 生成数据
    au1 = Author(name="老王")
    au2 = Author(name="老惠")
    au3 = Author(name="老刘")
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name="老王回忆录", author_id=au1.id)
    bk2 = Book(name="我读书少，你别骗我", author_id=au1.id)
    bk3 = Book(name="如何才能让自己变骚", author_id=au2.id)
    bk4 = Book(name="怎样征服美丽少女", author_id=au3.id)
    bk5 = Book(name="如何征服英俊少年", author_id=au3.id)
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    db.session.commit()
    app.run(debug=True)
