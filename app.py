from flask import Flask

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

@app.route(/double)
def double():
    value = request.args.get('n')
    return jsonify({"result": int(value) * 2}), 200

if __name__ == "__main__":
    app.run(debug=True)