from django.http.response import HttpResponseRedirectBase


class ResponseRedirectException(Exception):
    def __init__(self, response):
        assert isinstance(response, HttpResponseRedirectBase)
        self.response = response
