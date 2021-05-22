import os

from flask import Flask, request, jsonify
from login_blueprint import login_bp

app = Flask(__name__)

app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0")
