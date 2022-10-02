from pws.consts import HTTPConsts


class Response:
    def __init__(self, content, response_code, context,
                 content_type=HTTPConsts.HTMLContentType, protocol=HTTPConsts.HTTPProtocol):

        self.content = content
        self.response_code = response_code
        self.context = context
        self.content_type = content_type
        self.protocol = protocol

    def create_response_header(self):
        response_header = HTTPConsts.Response.format(
            protocol=self.protocol,
            response_code=self.response_code,
            content_type=self.content_type
        )

        return response_header
