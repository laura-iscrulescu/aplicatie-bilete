import json

from flask import Blueprint
from flask_json import as_json
from flask.globals import request
import requests 

controllers_bp = Blueprint('controllers_bp', __name__)

LOGIN_SERVICE_URL = 'http://app-login:5001/authorize'

def logged_in(token: str):
    data = {'token': token}
    r = requests.post(LOGIN_SERVICE_URL, data)
    print("Executing authorization")
    print(r)
    if r.status_code == 200:
        return True
    return False

from app import db_cursor

@as_json
@controllers_bp.route('/shows', methods=["GET"])
def shows():
    ''' Returns details about all the shows available '''
    _shows = db_cursor.show.find()

    item = {}
    data = []
    for show in _shows:
        print(show)
        item = {
            'id': str(show['_id']),
            'show': json.dumps(show, default=str)
        }
        data.append(item)

    return {
        'data': data
        }, 200

@as_json
@controllers_bp.route('/show/<string:show>', methods=["GET"])
def show(show):
    ''' Returns details about the show provided in the request '''
    _shows = db_cursor.show.find({
        'location' : show
    })
    data = []
    for show in _shows:
        print(show)
        item = {
            'id': str(show['_id']),
            'show': json.dumps(show, default=str)
        }
        data.append(item)
    
    return {
        'data': data
        },200

@controllers_bp.route('/show', methods=["POST"])
def insert_show():
    ''' Returns details about the show provided in the request '''
    data = request.form
    date = data.get('date')
    location = data.get('location')
    seats = data.get('seats')
    artists = data.get('artists')
    price = data.get('price')
    token = data.get('token')
    if logged_in(token):
        db_cursor.show.insert_one({
            'date': date,
            'location': location,
            'seats': seats,
            'artists': artists,
            'price': price
        })
        return "Show inserted"
    return 'Authorization failed'

@controllers_bp.route('/book', methods=["POST"])
def book():
    ''' 
        Book a seat at a show
        @arg1 : show
        @arg2 : day
        @arg3 : seat
    '''
    data = request.form
    
    location = data.get('location')
    artists = data.get('artists')
    seats = data.get('seats')
    
    show = db_cursor.show.find_one({
        'location': location,
        'artists':  artists
    })
    
    updated_seats = int(show['seats']) - int(seats)
    
    newvalues = { "$set": { "seats": updated_seats } }


    db_cursor.show.update_many({
        'location': location,
        'artists':  artists
    },newvalues)
    
    
    return "Booked {} seats".format(seats)


@controllers_bp.route('/cancel', methods=["POST"])
def cancel():
    ''' 
        Book a seat at a show
        @arg1 : show
        @arg2 : day
        @arg3 : seat
    '''
    data = request.form
    
    location = data.get('location')
    artists = data.get('artists')
    seats = data.get('seats')
    
    show = db_cursor.show.find_one({
        'location': location,
        'artists':  artists
    })
    
    updated_seats = int(show['seats']) + int(seats)
    
    newvalues = { "$set": { "seats": updated_seats } }


    db_cursor.show.update_many({
        'location': location,
        'artists':  artists
    },newvalues)
    
    return "Canceled  {} seats ".format(seats)
