from rest_framework.views import exception_handler as base_exception_handler


def exception_handler(exc, context):
    """Returns the response that should be used for any given exception."""
    response = base_exception_handler(exc, context)
    if response is not None:
        if isinstance(response.data, list):
            return response
        response.data["code"] = response.status_code
        if "detail" in response.data:
            response.data["error"] = response.data.pop("detail")
    return response
