from flask import jsonify, make_response


def input_list_result_response(list_result):
    """
    Get the input list result
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': 'success',
        'input_list': list_result
    })), 200


def input_list_sum_result_response(list_sum):
    """
    Get the sum of input list result
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': 'success',
        'total': list_sum
    })), 200


def error_response(status, message, status_code):
    """
    :param status: Status message
    :param message: Response Message
    :param status_code: Http response code
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code


def error_obj(message, status_code):
    """
    :param message: Response Message
    :param status_code: Http response code
    :return: Http Json response
    """
    return jsonify({
        'message': message,
        'status_code': status_code,
    })
