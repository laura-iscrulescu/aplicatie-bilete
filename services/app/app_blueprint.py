from flask import Blueprint
from flask_json import as_json

controllers_bp = Blueprint('controllers_bp', __name__)

from app import db_cursor
@controllers_bp.route('/shows', methods = ["GET"])
@as_json
def shows():
    ''' Returns details about all the shows available '''
    _shows = db_cursor.show.find()

    item = {}
    data = []
    for show in _shows:
        item = {
            'id': str(show['_id']),
            'show': show['show']
        }
        data.append(item)

    return {
        'status': True,
        'data': data
    }

@controllers_bp.route('/show/<string:show>', methods = ["GET"])
def show(show):
    ''' Returns details about the show provided in the request '''
    return "Hello 2!"

@controllers_bp.route('/seats/<show>/<int:day>', methods = ["GET"])
def seats(show, day):
    ''' Return details about the seats for that show '''
    return "Hello 1!"

@controllers_bp.route('/book', methods = ["POST"])
def book():
    ''' 
        Book a seat at a show
        @arg1 : show
        @arg2 : day
        @arg3 : seat
    '''
    return "Hello 3!"

@controllers_bp.route('/cancel', methods = ["POST"])
def cancel():
    ''' 
        Book a seat at a show
        @arg1 : show
        @arg2 : day
        @arg3 : seat
    '''
    return "Hello 3!"
