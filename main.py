from controller import Controller
from pws.server import Server
from config import Config


def init_board(controller):
    controller.disconnect_from_network()
    controller.connect_to_network(Config.NETWORK_SSID, Config.NETWORK_PASSWORD)


def init_web_server(server):
    server.init_server()
    server.run()


def main():
    controller = Controller()
    init_board(controller)

    web_server = Server()
    init_web_server(web_server)


if __name__ == "__main__":
    main()
