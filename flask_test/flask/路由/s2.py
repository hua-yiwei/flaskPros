from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"], endpoint="n1")
def index():
    # 反向生成url
    # 访问/index页面会输出以下路由
    n1 = url_for("n1")
    n2 = url_for("n2")
    n3 = url_for("n3")
    print(n1)
    print(n2)
    print(n3)
    # 不使用endpoint取别名，默认是函数名
    print(url_for("morenfun"))
    return "hello world"


@app.route("/login", methods=["GET", "POST"], endpoint="n2")
def login():
    return "login"


@app.route("/logout", methods=["GET", "POST"], endpoint="n3")
def logout():
    return "logout"


@app.route("/moren")
def morenfun():
    return "moren"


if __name__ == '__main__':
    app.run()
