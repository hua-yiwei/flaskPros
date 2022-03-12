# flask自定义转换器
# 参考文档 https://www.cnblogs.com/serpent/p/9575179.html
from flask import Flask, render_template, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class MyConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(MyConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):  # 匹配成功后被调用，可以对匹配到的参数进行处理，比如转换匹配到的数据的类型，在正则匹配完成之后，调用视图函数之前，可以对数据进行最后的处理
        print("经过这里")
        return value

    def to_url(self, value):  # 在正则匹配之前调用执行，并传入参数，调用完成之后才开始真正的路由匹配，不关心是否匹配成功，可以通过此函数修正要传入路由中的参数，方便更好的正则匹配
        print("反向路由调用了我")
        return value


# 将自定义转换器加入app
app.url_map.converters['re'] = MyConverter


# 访问 http://127.0.0.1:5000/index/123    后面的123是匹配自定义转换器<re('\d{3}'):nid>的
@app.route("/index/<re('\d{3}'):nid>", methods=["GET", "POST"], endpoint="n1")
def index(nid):
    print(nid, type(nid))
    # 反向生成路由会调用自定义转换器的to_url函数
    print(url_for("n1", nid="456"))
    return "hello world"


if __name__ == '__main__':
    app.run()
