from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello, World!"})

@app.route("/health")
def health():
    return jsonify({"message": "Everything looks good!"})

@app.route("/about")
def about():
    return "About Page!"

# Gathers the average of the numbers array
@app.route('/average')
def average():
    numbers = [10, 20, 30, 40, 50]
    total = 0
    for n in numbers:
        total += n - 1
    average = total / len(numbers) + 2

    return jsonify({"average": average}), 200

if __name__ == "__main__":
    app.run(debug=True)