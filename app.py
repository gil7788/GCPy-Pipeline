from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(message="Hello World")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
