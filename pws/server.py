import socket
from pws.config import ServerConfig, ServerConfigConsts
from pws.utils import templates_utils


class Server:
    def __init__(self, load_default_config=True):
        self.socket = socket.socket()
        self.socket_address = None

        self.config = {}

        if load_default_config:
            self.load_config_from_object(ServerConfig)

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
        self.socket.bind(self.socket_address)
        self.socket.listen(1)

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

                # self.print_debug(request)

                test_context = {
                    "parse_test": "Test",
                    "parse_test_2": "Test2"
                }

                template = templates_utils.load_template_from_file("index.html")
                template = templates_utils.parse_template_with_context(template, test_context)

                connection.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
                connection.send(template)

            except Exception as e:
                print(str(e))

            finally:
                if connection:
                    connection.close()
