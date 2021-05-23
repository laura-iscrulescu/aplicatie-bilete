import os

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_json import FlaskJSON

app = Flask(__name__)
json = FlaskJSON(app)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' +  os.environ['MONGODB_DATABASE'] 

mongo = PyMongo(app)
db_cursor = mongo.db

from app_blueprint import controllers_bp
app.register_blueprint(controllers_bp, url_prefix='/api')


if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0")