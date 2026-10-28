from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>DevOps App</title></head>
        <body>
            <h1>Welcome to the DevOps Lifecycle Project!</h1>
            <p>Flask application is running successfully.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
