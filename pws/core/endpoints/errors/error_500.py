from pws.core.endpoints.errors.error_base import ErrorBase


class Error500(ErrorBase):
    def __init__(self):
        super().__init__()

        self.status_code = 500
        self.response_code = "500 Internal Server Error"
