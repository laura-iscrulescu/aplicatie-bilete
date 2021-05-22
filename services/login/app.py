import os
import secrets
import pymongo

from flask import Flask
from flask.globals import request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(app)
db = mongo.db
users = db['users']

@app.route('/create', methods=["POST"])
def create():
    data = request.form
    username = data.get('user')
    password = data.get('password')

    users.insert_one({'user': username, 'pass': password, 'hash': ""})

    return  "User created"


@app.route('/login', methods=["POST"])
def login():
    data = request.form
    username = data.get('user')
    password = data.get('password')
    hash = secrets.token_hex(nbytes=16)
    newvalues = { "$set": { "hash": hash } }
    
    user = users.find_one({'user': username, 'pass': password})
    if user:
        users.update_one({'user': username, 'pass': password}, newvalues)
        return hash
    return 'User not found',403


@app.route('/authorize', methods=["POST"])
def authorize():
    data = request.form
    jwt = data.get('token')
    _users = users.find()
    for user in _users:
        print(user)
        if user['hash'] == jwt:
            return 'Authorized'
    return  'User not found', 403


@app.route('/logout', methods=["POST"])
def logout():
    data = request.form
    username = data.get('user')
    password = data.get('password')
    newvalues = { "$set": { "hash": "" } }
    users.update_one({'user': username, 'pass': password}, newvalues)
    return "User logged out"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
