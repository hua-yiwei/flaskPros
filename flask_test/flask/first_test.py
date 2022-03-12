from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/', endpoint="n1")
def index():
    data = {
        "name": "张三"
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
