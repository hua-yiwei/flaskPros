from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {
        "words": "hello world"
    }
    return render_template("index.html", **context)


def my_filter(string):
    my_string = ""
    for i in string:
        my_string = my_string + i + "*"
    my_string.strip("*")
    return my_string


# 注册过滤器，第一个参数是函数，第二个参数是调用时使用的名称
# 调用看 index.html
app.add_template_filter(f=my_filter, name="woziji")

if __name__ == '__main__':
    app.run()
