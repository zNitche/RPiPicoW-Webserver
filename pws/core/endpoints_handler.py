from pws.core.endpoints.home_endpoint import HomeEndpoint
from pws.core.endpoints.errors.error_404 import Error404
from pws.core.endpoints.errors.error_500 import Error500


class EndpointsHandler:
    def __init__(self):
        self.endpoints = [
            HomeEndpoint()
        ]

        self.errors_endpoints = [
            Error404(),
            Error500()
        ]

    def handle_request(self, request):
        endpoint = self.get_endpoint_for_request(request)
        response = self.handle_error(404)

        if endpoint:
            response = endpoint.process()

        return response

    def handle_error(self, error_code):
        error_endpoint = self.get_error_by_code(error_code)
        response = self.get_error_by_code(404).process()

        if error_endpoint:
            response = error_endpoint.process()

        return response

    def get_error_by_code(self, error_code):
        error_endp = None

        for error_endpoint in self.errors_endpoints:
            if error_code == error_endpoint.status_code:
                error_endp = error_endpoint

        return error_endp

    def get_endpoint_for_request(self, request):
        endp = None

        if request:
            for endpoint in self.endpoints:
                if request.method in endpoint.methods and request.endpoint == endpoint.address:
                    endp = endpoint

        return endp
