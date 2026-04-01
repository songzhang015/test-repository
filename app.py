from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/health")
def health():
    return "Everything looks good!"

@app.route("/about")
def about():
    return "About Page!"

@app.route('/average')
def average():
    numbers = [10, 20, 30, 40, 50]
    total = 0
    for n in numbers:
        total += n
    average = total / len(numbers) + 1

    return jsonify({"average": average}), 200

if __name__ == "__main__":
    app.run(debug=True)