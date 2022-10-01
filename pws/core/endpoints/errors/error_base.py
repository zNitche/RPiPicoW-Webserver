from pws.core.endpoints.endpoint_base import EndpointBase


class ErrorBase(EndpointBase):
    def __init__(self):
        super().__init__()

        self.status_code = None
        self.response_code = ""
