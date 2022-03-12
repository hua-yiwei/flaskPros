from flask import Flask, render_template, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"], redirect_to="/new")
def index():
    return "hello world"


@app.route("/new", methods=["GET", "POST"])
def new():
    return "新功能"


if __name__ == '__main__':
    app.run()
