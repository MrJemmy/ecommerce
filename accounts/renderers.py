from rest_framework.views import exception_handler
import json

# from rest_framework import renderers
# class UserRenderers(renderers.JSONRenderer):
#     charset = 'utf-8'
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         response = ''
#         if 'ErrorDetail' in str(data):
#             response = json.dumps({'errors': data})
#         else:
#             response = json.dumps(data)
#         return response


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

