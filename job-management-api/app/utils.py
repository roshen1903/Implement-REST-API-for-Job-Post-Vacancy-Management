from flask import jsonify

def create_response(data=None, message=None, status_code=200):
    """
    Create a standard JSON response.

    :param data: Data to include in the response (default: None)
    :param message: Message to include in the response (default: None)
    :param status_code: HTTP status code (default: 200)
    :return: Flask response object
    """
    response = {
        "status": "success" if status_code < 400 else "error",
        "message": message,
        "data": data,
    }
    return jsonify(response), status_code


def validate_request_data(required_fields, request_data):
    """
    Validate if required fields exist in request data.

    :param required_fields: List of required field names
    :param request_data: The data to validate
    :return: Tuple (is_valid, missing_fields)
    """
    missing_fields = [field for field in required_fields if field not in request_data]
    return len(missing_fields) == 0, missing_fields
