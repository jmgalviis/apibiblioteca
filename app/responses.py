from flask import jsonify


def response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ), 200


def bad_request():
    return jsonify({
        'success': False,
        'data': {},
        'messages': 'Bad Request',
        'code': 400
    }), 400


def not_found():
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': 'Resource not found',
            'code': 404
        }
    ), 404
