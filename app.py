from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!!! :3"

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    num1 = request.args.get("num1", "")
    num2 = request.args.get("num2", "")

    if not num1:
        num1 = 0
    if not num2:
        num2 = 0

    num1 = float(num1)
    num2 = float(num2)

    resp = (num1+num2 > 5.8)*1

    return jsonify({"prediction": resp}, {"features": {"num1": num1, "num2": num2}})

if __name__ == '__main__':
    app.run(port=5005)
    # app.run(port=5000)
