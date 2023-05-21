import logging


class LogRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger()

    def __call__(self, request):
        self.logger.debug(
            f"Incoming request: {request.method} {request.get_full_path()}")
        for header, value in request.headers.items():
            self.logger.debug(f"Header: {header} = {value}")
        response = self.get_response(request)
        return response
