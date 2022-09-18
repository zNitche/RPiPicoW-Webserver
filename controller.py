import machine
import network
import time
from config import Config


class Controller:
    def __init__(self):
        self.print_debug_logs = True

        self.wlan = self.init_wlan()

        self.onboard_led = machine.Pin("LED", machine.Pin.OUT)

        self.toggle_onboard_led(True)

    def print_debug(self, content):
        if self.print_debug_logs:
            print(content)

    def toggle_onboard_led(self, state):
        self.onboard_led.on() if state else self.onboard_led.off()

    def blink_onboard_led(self, blinks_count, time_between):
        for i in range(blinks_count):
            self.toggle_onboard_led(False)
            time.sleep(1)
            self.toggle_onboard_led(True)

            time.sleep(time_between)

    def init_wlan(self):
        self.print_debug("WLAN init...")

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

        return wlan

    def activate_wlan_if_disabled(self):
        if not self.wlan.active():
            self.print_debug("Enabling WLAN interface...")

            self.wlan.active(True)

    def connect_to_network(self, ssid, password):
        attempts = 0

        self.activate_wlan_if_disabled()

        self.print_debug("Connecting to WIFI network...")

        while not self.wlan.isconnected() and attempts < Config.MAX_WIFI_RECONNECT_ATTEMPTS:
            self.print_debug("Trying to establish WiFi connection...")
            self.blink_onboard_led(Config.WIFI_CONNECTING_BLINKS_COUNT, 2)

            self.wlan.connect(ssid, password)

            time.sleep(1)

            attempts += 1

        if self.wlan.isconnected():
            self.print_debug(f"Connected to '{ssid}' network...")

            self.blink_onboard_led(Config.WIFI_CONNECTED_BLINKS_COUNT, 1)

        else:
            self.print_debug("Failed to connect...")

    def disconnect_from_network(self):
        self.print_debug("Disconnecting from network...")

        if self.wlan.isconnected():
            self.wlan.disconnect()

    def get_wlan_config(self):
        config = None

        if self.wlan.active() and self.wlan.isconnected():
            config = self.wlan.ifconfig()

        return config

    def get_wifi_networks(self):
        self.print_debug("Getting wifi networks...")

        self.activate_wlan_if_disabled()

        networks = self.wlan.scan()

        return networks