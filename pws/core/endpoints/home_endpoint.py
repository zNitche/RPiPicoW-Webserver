from pws.core.endpoints.endpoint_base import EndpointBase
from pws.consts import EndpointsConsts, HTTPConsts


class HomeEndpoint(EndpointBase):
    def __init__(self):
        super().__init__()

        self.template = "index.html"
        self.methods = [EndpointsConsts.GET_REQUEST]
        self.address = "/"

    def process(self):
        template = self.template
        response_code = HTTPConsts.OK_RESPONSE

        context = {
            "parse_test": "Hello 1",
            "parse_test_2": "Hello 2"
        }

        return context, template, response_code
