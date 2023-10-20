import urequests as requests
import json
import time
import network
try:
    from WIFI_CONFIG import SSID, PSK
except ImportError:
    print("Create WIFICONFIG.py with your WiFi credentials")
    
# Enable the Wireless
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def network_connect(SSID, PSK):

    # Number of attempts to make before timeout
    max_wait = 5

    # Sets the Wireless LED pulsing and attempts to connect to your local network.
    print("connecting...")
    wlan.config(pm=0xa11140)  # Turn WiFi power saving off for some slow APs
    wlan.connect(SSID, PSK)

    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    # Handle connection error. Switches the Warn LED on.
    if wlan.status() != 3:
        print("Unable to connect. Attempting connection again")
try:
    network_connect(SSID, PSK)
except NameError:
    print("Create WIFI_CONFIG.py with your WiFi credentials")
def fuck():        
    while True:
            url = "https://script.google.com/macros/s/AKfycbzgaTWDLhNsxe1YhWafK3ofqEc93cAs3XNjz0IEhbiqRvCqwyv_AKMyb3ueIeu9Bgc/exec"
            headers = {
                "accept": "application/json"
            }
            page = requests.get(url)
            return page.json()
