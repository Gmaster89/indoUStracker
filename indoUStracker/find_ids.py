import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

symbols = [
    'TCS', 'INFY', 'HCLTECH', 'TITAN', 'RELIANCE', 'HDFCBANK', 'ICICIBANK',
    'BHARTIARTL', 'LT', 'TATAMOTORS', 'WIPRO', 'LTIM', 'SUNPHARMA', 'CIPLA',
    'ASIANPAINT', 'MARUTI', 'NTPC', 'ONGC', 'SBIN', 'KOTAKBANK', 'AXISBANK',
    'LUPIN', 'CRISIL', 'TECHM', 'BAJAJFINSV'
]

# Note: The autosuggest API requires a User-Agent, but some APIs might block standard Python agents.
# Let's try to query the Yahoo Finance API from server side? No, the goal is client-side.
# Wait, I just need the Moneycontrol IDs.
# I can just use DuckDuckGo Lite search from Python to find the Moneycontrol URL for each symbol.
import urllib.parse
from html.parser import HTMLParser

def get_mc_id(symbol):
    query = urllib.parse.quote(f"site:moneycontrol.com/india/stockpricequote {symbol}")
    url = f"https://lite.duckduckgo.com/lite/"
    req = urllib.request.Request(url, data=urllib.parse.urlencode({'q': query}).encode('utf-8'), headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        # Find the first moneycontrol URL
        # example: https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT
        import re
        match = re.search(r'https://www.moneycontrol.com/india/stockpricequote/[^/]+/[^/]+/([^/"\'<>\s]+)', html)
        if match:
            return match.group(1)
        return None
    except Exception as e:
        return str(e)

results = {}
for sym in symbols:
    results[sym] = get_mc_id(sym)
    print(f"{sym}: {results[sym]}")

with open('mc_ids.json', 'w') as f:
    json.dump(results, f)
