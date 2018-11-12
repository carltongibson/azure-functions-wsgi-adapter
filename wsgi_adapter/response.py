

class StartResponseWrapper:
    def __call__(self, status, response_headers, exc_info=None):
        self.status = status
        self.headers = response_headers
        self.exc_info = exc_info
