from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call the default exception handler to get the standard error response.
    response = exception_handler(exc, context)

    # Check if a response was generated.
    if response is not None:
        # Create a custom response format with 'error' as the key and the error message as the value.
        custom_response = {
            'errors': response.data
        }
        response.data = custom_response

    return response

