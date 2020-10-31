from flask import Flask, request
import app.list_sum as list_sum
import app.const as const
from app import app
from app.helper import input_list_result_response, input_list_sum_result_response, error_response


@app.route('/input_list', methods=['GET'])
def get_input_list():
    input_list_result = const.NUMBERS_TO_ADD
    return input_list_result_response(input_list_result)


@app.route('/total', methods=['GET'])
def get_sum_input_list():
    input_list_sum_result = list_sum.get_list_sum()
    if not const.HTTP_ERROR:
        return input_list_sum_result_response(input_list_sum_result)
    else:
        return error_response('HTTP error', input_list_sum_result['message'], input_list_sum_result['status_code'])
