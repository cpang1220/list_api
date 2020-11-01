import app.const as const
import requests
from app.helper import error_obj
from flask import json


def get_list_sum():
    const.HTTP_ERROR = False
    input_list_response = requests.get(const.LOCALHOST_API_URL + '/input_list')
    try:
        input_list_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        const.HTTP_ERROR = True
        status_code = e.response.status_code
        message = e.response.reason
        return error_obj(message,status_code)
    input_list_obj = json.loads(input_list_response.content)
    input_list_sum_result = sum(input_list_obj['input_list'])
    return input_list_sum_result

