from flask import Flask

app = Flask(__name__)
app.secret_key = "sdfgsdfhsdgf"


@app.route("/x1")
def x1():
    return "视图函数x1"


class MiddleWare(object):
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        """
        每次有请求时
        :param args:
        :param kwargs:
        :return:
        """
        print("before")
        print(environ)
        obj = self.old_wsgi_app(environ, start_response)
        print("after")
        return obj


if __name__ == '__main__':
    app.wsgi_app = MiddleWare(app.wsgi_app)
    app.run()
    # app.__call__
    """
    小知识：obj() ->对象加括号，会执行对象的__call__方法
    每次有请求来时首先执行的步骤
    1、app.__call__
    2、app.wsgi_app
    """
