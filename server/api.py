from flask import jsonify, Blueprint, request
from server.database import *

api = Blueprint('api', __name__, url_prefix='/api')


def error(code, message):
    json = {
        'error': {
            'code': code,
            'message': message
        }
    }

    return jsonify(json)


@api.before_request
def check_api_key():
    if request.method == 'POST':
        key = request.form.get('key')

        if not key:
            return error('001', 'API key missing')

        query = APIkey.query.filter_by(key=key).first()

        if not query:
            return error('100', 'API key invalid')
    return error('000', 'No data received')


@api.route('/createOrder', methods=('GET', 'POST'))
def create_order():
    if request.method == 'POST':
        pass