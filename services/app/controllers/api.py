from flask import Blueprint

controllers_bp = Blueprint('controllers_bp', __name__)

@controllers_bp.route('/seats', methods = ["GET"])
def seats():
    return "Hello 1!"

@controllers_bp.route('/shows', methods = ["GET"])
def shows():
    return "Hello 2!"

@controllers_bp.route('/book', methods = ["GET"])
def book():
    return "Hello 3!"

@controllers_bp.route('/cancel', methods = ["GET"])
def cancel():
    return "Hello 3!"
