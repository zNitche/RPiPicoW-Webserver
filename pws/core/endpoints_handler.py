from pws.consts import HTTPConsts

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

        if endpoint:
            response_header = HTTPConsts.Response.format(
                protocol=HTTPConsts.HTTPProtocol,
                response_code="200 OK",
                content_type=HTTPConsts.HTMLContentType
            )

            response_content = endpoint.template
            response_context = endpoint.get_context()

        else:
            response_header, response_content, response_context = self.handle_error(404)

        return response_header, response_content, response_context

    def handle_error(self, error_code):
        error_endpoint = self.get_error_by_code(error_code)

        response_header = None
        response_content = None
        response_context = {}

        if error_endpoint:
            response_header = HTTPConsts.Response.format(
                protocol=HTTPConsts.HTTPProtocol,
                response_code=error_endpoint.response_code,
                content_type=HTTPConsts.HTMLContentType
            )

            response_content = error_endpoint.template
            response_context = error_endpoint.get_context()

        return response_header, response_content, response_context

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
