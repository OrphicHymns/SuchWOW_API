from flask import Flask, jsonify
import requests
import wownero


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "API is working fine"


@app.route("/api")
def suchwow():
    return jsonify(wownero.wownero())


if __name__ == "__main__":
    #app.debug = True
    app.run(host="0.0.0.0",port= 5000)