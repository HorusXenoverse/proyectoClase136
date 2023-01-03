from flask import Flask, jsonify, request
from dataArchivosStar import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"success"
    }), 200

@app.route("/star")
def planetIndex():
    name = request.args.get("name")
    starName = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": starName,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()