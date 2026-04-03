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

if __name__ == "__main__":
    app.run(debug=True)