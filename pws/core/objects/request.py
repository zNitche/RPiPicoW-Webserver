class Request:
    def __init__(self, request_string):
        self.request_string = request_string.decode("utf-8")

        self.method = ""
        self.endpoint = ""

        self.create_from_request()

    def create_from_request(self):
        splitted_request = self.request_string.split()

        self.method = splitted_request[0]
        self.endpoint = splitted_request[1]

    def __str__(self):
        return f"Request (method={self.method}, endpoint={self.endpoint})"
