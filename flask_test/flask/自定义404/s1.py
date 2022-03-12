from flask import Flask, abort

app = Flask(__name__)


@app.route("/")
def index():
    abort(404)  # 抛出404错误
    return


@app.errorhandler(404)
def handle_404(err):
    print(err)
    return "这个是自定义404"


if __name__ == '__main__':
    app.run()
