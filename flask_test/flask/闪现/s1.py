from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = "sdfgsdfhsdgf"

@app.route("/x1")
def x1():
    flash("只能看一次的数据")   # 要先设置app.secret_key不然会出错
    return "视图函数x1"


@app.route("/x2")
def x2():
    data = get_flashed_messages()
    print(data)
    return "视图函数x2"


if __name__ == '__main__':
    app.run()
