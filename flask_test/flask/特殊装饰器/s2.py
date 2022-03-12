from flask import Flask, render_template, redirect

app = Flask(__name__)

"""如果视图函数执行前函数有返回值，就会跳过视图函数"""
@app.before_request  # 视图函数执行前
def before1():
    print("视图函数执行前1")
    return "视图函数执行前1直接返回"


@app.before_request  # 视图函数执行前
def before2():
    print("视图函数执行前2")

@app.after_request  # 视图函数执行前,执行这个装饰器，flask默认传入response，因此after函数要接收参数
def after1(response):
    print("视图函数执行后1")
    return response


@app.after_request  # 视图函数执行前,执行这个装饰器，flask默认传入response，因此after函数要接收参数
def after2(response):
    print("视图函数执行后2")
    return response


@app.route("/index", methods=["GET", "POST"])
def index():
    print("index")
    return "hello world"


@app.route("/order", methods=["GET", "POST"])
def order():
    print("order")
    return "order"


if __name__ == '__main__':
    app.run()
