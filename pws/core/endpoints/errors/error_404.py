from pws.core.endpoints.errors.error_base import ErrorBase


class Error404(ErrorBase):
    def __init__(self):
        super().__init__()

        self.status_code = 404
        self.response_code = "404 Not found"
