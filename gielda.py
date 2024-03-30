import requests
import time

# Konfiguracja
API_URL = "https://api.coingecko.com/api/v3/simple/price"
CRYPTOS = ["bitcoin", "ethereum", "ripple", "dogecoin"]
CURRENCY = "usd"
INTERVAL = 60  

def get_prices():
    params = {
        'ids': ','.join(CRYPTOS),
        'vs_currencies': CURRENCY,
    }
    response = requests.get(API_URL, params=params)
    response.raise_for_status()  
    return response.json()

def monitor():
    previous_prices = {}
    while True:
        current_prices = get_prices()
        for crypto in CRYPTOS:
            price = current_prices[crypto][CURRENCY]
            if crypto in previous_prices:
                if price > previous_prices[crypto]:
                    print(f"{crypto.upper()}: cena rośnie ({price})")
                elif price < previous_prices[crypto]:
                    print(f"{crypto.upper()}: cena spada ({price})")
                else:
                    print(f"{crypto.upper()}: cena bez zmian ({price})")
            else:
                print(f"{crypto.upper()}: aktualna cena {price}")
            previous_prices[crypto] = price
        time.sleep(INTERVAL)


monitor()
   
