from flask import Flask, request, jsonify
from flask_cors import CORS  # allow frontend to connect

app = Flask(__name__)
CORS(app)  # enable CORS

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    num1 = float(data.get("num1", 0))
    num2 = float(data.get("num2", 0))
    operation = data.get("operation")

    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
