from pws.core.endpoints.endpoint_base import EndpointBase


class ErrorBase(EndpointBase):
    def __init__(self):
        super().__init__()

        self.status_code = None
        self.response_code = ""

        self.template = "error.html"

    def process(self):
        return {
            "error_code": self.status_code
        }
