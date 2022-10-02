from pws.core.endpoints.endpoint_base import EndpointBase
from pws.core.objects.response import Response


class ErrorBase(EndpointBase):
    def __init__(self):
        super().__init__()

        self.status_code = None
        self.response_code = ""

        self.template = "error.html"

    def process(self):
        template = self.template
        context = {
            "error_code": self.status_code
        }

        return Response(template, self.response_code, context)
