
from flask import Flask, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Calculator App deployed successfully!",
        "version": "v1"
    })

@app.route("/add/<int:a>/<int:b>")
def addition(a, b):
    return jsonify({"result": add(a, b)})

@app.route("/subtract/<int:a>/<int:b>")
def subtraction(a, b):
    return jsonify({"result": subtract(a, b)})

@app.route("/multiply/<int:a>/<int:b>")
def multiplication(a, b):
    return jsonify({"result": multiply(a, b)})

@app.route("/divide/<int:a>/<int:b>")
def division(a, b):
    if b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    return jsonify({"result": divide(a, b)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
