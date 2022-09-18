from controller import Controller
from config import Config


def main():
    controller = Controller()

    controller.connect_to_network(Config.NETWORK_SSID, Config.NETWORK_PASSWORD)

    print(controller.wlan.isconnected())


if __name__ == "__main__":
    main()
