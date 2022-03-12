from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = "sdfgsdfhsdgf"

@app.route("/x1")
def x1():
    flash("只能看一次的数据,分类a", category="a")   # 要先设置app.secret_key不然会出错
    flash("这个是分类b", category="b")
    return "视图函数x1"


@app.route("/x2")
def x2():
    data = get_flashed_messages(category_filter=["a"])
    print(data)
    return "视图函数x2"


@app.route("/x3")
def x3():
    data = get_flashed_messages(category_filter=["b"])
    print(data)
    return "视图函数x3"


if __name__ == '__main__':
    app.run()
