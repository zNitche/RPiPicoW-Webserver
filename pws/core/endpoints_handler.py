from pws.core.endpoints.home_endpoint import HomeEndpoint


class EndpointsHandler:
    def __init__(self):
        self.endpoints = [
            HomeEndpoint()
        ]

    def handle_request(self, request):
        endpoint = self.get_endpoint_for_request(request)

        response_header = "HTTP/1.0 404 Not found\r\nContent-type: text/html\r\n\r\n"
        response_content = None
        response_context = {}

        if endpoint:
            response_header = "HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n"
            response_content = endpoint.template
            response_context = endpoint.get_context()

        return response_header, response_content, response_context

    def get_endpoint_for_request(self, request):
        endp = None

        if request:
            for endpoint in self.endpoints:
                if request.method in endpoint.methods and request.endpoint == endpoint.address:
                    endp = endpoint

        return endp
