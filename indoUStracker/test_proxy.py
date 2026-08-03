import urllib.request

try:
    url = "https://thingproxy.freeboard.io/fetch/https://query1.finance.yahoo.com/v7/finance/quote?symbols=RELIANCE.NS"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    print(urllib.request.urlopen(req).read().decode('utf-8'))
except Exception as e:
    print(e)
