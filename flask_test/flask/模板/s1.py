from flask import Flask, render_template, Markup

app = Flask(__name__)


@app.template_global()    # 在每一个模板中都加入sbbb函数
def sbbb(a1, a2):
    return a1 + a2


def gen_input(val):
    return "<input value='%s' />" % val


def gen_input_2(val):
    return Markup("<input value='%s' />" % val)


@app.route("/index")
def index():
    context = {
        "k1": 33,
        "k2": [11, 22, 33],
        "k3": {"name": "oldboy", "age": 87},
        "k4": lambda x: x + 1,
        "k5": gen_input,
        "k6": gen_input_2
    }
    return render_template("index.html", **context)


if __name__ == '__main__':
    app.run()
