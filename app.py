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

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"}), 200

if __name__ == "__main__":
    app.run(debug=True)