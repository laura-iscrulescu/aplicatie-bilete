from flask import Blueprint

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/create', methods = ["POST"])
def create():
    ''' Returns details about all the shows available '''
    data = []

    return {
        'status': True,
        'data': data
    }

@login_bp.route('/login', methods = ["POST"])
def login():
    ''' Returns details about the show provided in the request '''
    return "Hello 2!"

@login_bp.route('/logout', methods = ["POST"])
def logout():
    ''' Returns details about the show provided in the request '''
    return "Hello 2!"