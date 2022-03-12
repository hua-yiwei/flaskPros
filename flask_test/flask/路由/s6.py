from flask import Flask, render_template, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route("/new", methods=["GET", "POST"])
def index():
    return "hello world"


if __name__ == '__main__':
    app.run()
