from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    return "hello world"


def order():
    return "order"


# 添加路由的另一种方式。app.route()的本质就是内部执行了add_url_rule方法
app.add_url_rule(rule="/order", view_func=order)

if __name__ == '__main__':
    app.run()
