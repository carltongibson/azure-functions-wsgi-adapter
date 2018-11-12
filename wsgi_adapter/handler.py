import os

import azure.functions as func
from django.http.response import HttpResponse

from .request import AzureRequestAdapter
from .response import StartResponseWrapper


class AzureWSGIHandler:
    def __init__(self, wsgi_application):
        self.wsgi_application = wsgi_application

    def __call__(self, req):
        environ = AzureRequestAdapter(req).as_dict()
        start_response = StartResponseWrapper()
        django_response = self.wsgi_application(environ, start_response)
        return self._map_response(django_response, start_response)

    def _map_response(self, django_response, start_response):
        # TODO: We're cheating here. Handle as a WSGI Response, rather than a
        # djano response. (???: Allow framework specific strategies?)
        if isinstance(django_response, HttpResponse):
            azure_response = func.HttpResponse(
                body=django_response.content,
                status_code=django_response.status_code,
                headers=dict(start_response.headers),
                mimetype=django_response.get('Content-Type', ''),
                charset=django_response.charset
            )
        else:
            # Is FileResponse
            azure_response = func.HttpResponse(
                body=django_response.getvalue(),
                status_code=django_response.status_code,
                headers=dict(start_response.headers),
                mimetype=django_response.get('Content-Type', ''),
                charset=django_response.charset
            )

        return azure_response
