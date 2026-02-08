from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """Nginx Reverse Proxy Working 🎯
    server running by (Ankit kashyap)"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5055)
