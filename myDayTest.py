import urequests as requests
import json
import time
import network
from WIFI_CONFIG import SSID, PSK
# except ImportError:
#     print("Create WIFICONFIG.py with your WiFi credentials")

def network_connect(wlan):

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
        return False
    return True

def fuck():        
    url = "https://script.google.com/macros/s/AKfycbx1Pk7UFf7Cpn4Rn4SPc2sfPsHtc0zrol6WA6A5rWQevK4SGTvhTLxh2LY8JWX9KgSL/exec"
    headers = {
        "accept": "application/json"
    }
    print('huh')
    page = requests.get(url)
    psc = page.status_code
    while psc != 200:
        time.sleep(1)
        page = requests.get(url)
        print(page)
    print(page)
    pageData = page.json()
    page.close()
    return pageData
