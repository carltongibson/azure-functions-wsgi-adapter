import os

class AzureRequestAdapter:

    def __init__(self, azure_request):
        self.azure_request = azure_request

    def as_dict(self):
        """WSGI environ MUST be a plain Python dict."""
        req = self.azure_request

        path_info = req.route_params.get('path_info', '')
        path_info = '/' + os.getenv('FUNCTIONS_MOUNT_POINT') + '/' + path_info

        environ = {'HTTP_' + k.upper().replace('-', '_'): v for k, v in req.headers.items()}

        environ.update({
            "REQUEST_METHOD": req.method,
            "wsgi.input": req.get_body(),  # Wrap in io.BytesIO?
            "SERVER_NAME": "localhost",
            "SERVER_PORT": "7071",
            "PATH_INFO": path_info,
        })

        return environ
