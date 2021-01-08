#File that accesses API and return wanted data (price on DD-MM-YYYY)

#imports
import json
import time
import urllib.request

#functions
#function that returns price of DCR in EUR on the given date
def getPriceInEur(date):
    url = "https://api.coingecko.com/api/v3/coins/decred/history?date={}&localization=false"
    url = url.format(date)
    response = urllib.request.urlopen(url)
    jsonresponse = json.loads(response.read())
    return round(float(jsonresponse['market_data']['current_price']['eur']) , 2)
#function that stops sending requests after 90 attempts per minute
def wait():
    print('[!] Pausing process for ~ 1 minute.')
    time.sleep(65)
