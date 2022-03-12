from flask import Flask, render_template, redirect

app = Flask(__name__)

"""
所有使用@app.before_request装饰的函数会放到一个列表
before_request = [before1,before2]
"""


@app.before_request  # 视图函数执行前
def before1():
    print("视图函数执行前1")


@app.before_request  # 视图函数执行前
def before2():
    print("视图函数执行前2")


"""
所有使用@app.after_request装饰的函数会放到一个列表
after_request = [after1,after2]
但是会把列表进行反转 [after2,after1]
"""


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
