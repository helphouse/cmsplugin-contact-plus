from cmsplugin_contact_plus.exceptions import ResponseRedirectException


class ResponseRedirectMiddeleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, ResponseRedirectException):
            return exception.response
