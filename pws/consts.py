class EndpointsConsts:
    GET_REQUEST = "GET"
    POST_REQUEST = "POST"


class HTTPConsts:
    Response = "{protocol} {response_code}\r\nContent-type: {content_type}\r\n\r\n"

    HTTPProtocol = "HTTP/1.0"
    HTMLContentType = "text/html"

    OK_RESPONSE = "200 OK"
