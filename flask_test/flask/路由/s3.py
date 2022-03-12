from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/index/<int:nid>", methods=["GET", "POST"], endpoint="n1")
def index(nid):
    print(nid, type(nid))
    return "hello world"


if __name__ == '__main__':
    app.run()
