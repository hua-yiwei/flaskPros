from flask import Flask, session

app = Flask(__name__)
app.secret_key = "sadgsdfgsdfgdsfh"


@app.route("/index")
def index():
    session["k1"] = 123
    return "hello world"


@app.route("/order")
def order():
    print(session["k1"])
    return "order"


if __name__ == '__main__':
    app.run()
