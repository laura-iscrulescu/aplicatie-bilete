import os
import secrets
import pymongo

from flask import Flask
from flask.globals import request
from flask_pymongo import PyMongo


app = Flask(__name__)
db_uri = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' +  os.environ['MONGODB_DATABASE']
app.config["MONGO_URI"] = db_uri
mongo = PyMongo(app)
users = mongo.db.users

@app.route('/create', methods=["POST"])
def create():
    data = request.form
    username = data.get('user')
    password = data.get('password')

    users.insert_one({'user': username, 'pass': password, 'hash': ""})

    return {
        'status': 200,
        'respo': "User created"
    }


@app.route('/login', methods=["POST"])
def login():
    ''' Returns details about the show provided in the request '''
    data = request.form
    username = data.get('user')
    password = data.get('password')
    hash = secrets.token_hex(nbytes=16)
    newvalues = { "$set": { "hash": hash } }
    
    user = users.find_one({'user': username, 'pass': password})
    if user:
        users.update_one({'user': username, 'pass': password}, newvalues)
        return {
            'status': 200,
            'token': hash
        }
    return {
        'status': 403,
    }


@app.route('/authorize', methods=["POST"])
def authorize():
    data = request.form
    jwt = data.get('token')
    _users = users.find()
    for user in _users:
        if user.get(hash) == jwt:
            return {
            'status': 200,
        }
    return {
        'status': 403,
        'resp': 'User not found'
    }


@app.route('/logout', methods=["POST"])
def logout():
    ''' Returns details about the show provided in the request '''
    data = request.form
    username = data.get('user')
    password = data.get('password')
    newvalues = { "$set": { "hash": "" } }
    users.update_one({'user': username, 'pass': password}, newvalues)
    return {
        'status': 200,
        'resp': "User logged out"
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
