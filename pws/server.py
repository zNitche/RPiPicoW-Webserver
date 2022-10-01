import socket
from pws.config import ServerConfig, ServerConfigConsts
from pws.core.template_parser import TemplateParser
from pws.core.endpoints_handler import EndpointsHandler
from pws.core.objects.request import Request


class Server:
    def __init__(self, load_default_config=True):
        self.socket = socket.socket()
        self.socket_address = None

        self.config = {}

        if load_default_config:
            self.load_config_from_object(ServerConfig)

        self.template_parser = TemplateParser()
        self.endpoints_handler = EndpointsHandler()

    def load_config_from_object(self, config_object):
        if isinstance(config_object, dict):
            self.config = config_object

        else:
            self.config = config_object.__dict__

    def is_debug(self): \
            return True if \
                (ServerConfigConsts.CONFIG_DEBUG_KEY in self.config and self.config[
                    ServerConfigConsts.CONFIG_DEBUG_KEY]) \
                else False

    def print_debug(self, content):
        if self.is_debug():
            print(content)

    def get_socket_address(self):
        self.socket_address = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

    def bind_socket(self):
        self.print_debug("Binding socket...")

        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.socket_address)
        self.socket.listen(1)

        self.print_debug("Socket bound...")

    def init_server(self):
        self.get_socket_address()
        self.bind_socket()

    def run(self):
        self.mainloop()

    def mainloop(self):
        while True:
            connection = None

            try:
                connection, client_address = self.socket.accept()

                self.print_debug(f"client connected from: {client_address}")

                request = connection.recv(1024)
                self.print_debug(request)

                request = Request(request)
                self.print_debug(request)

                response_header, response_content, response_context = self.endpoints_handler.handle_request(request)

                connection.send(response_header)
                connection.send(self.template_parser.perform_parsing(response_content, response_context))

            except Exception as e:
                self.print_debug(str(e))

            finally:
                if connection:
                    connection.close()
