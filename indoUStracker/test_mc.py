import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ids = [
    'TCS', 'IT', 'HCL02', 'TI01', 'RI', 'HDF01', 'ICI02', 'BA08', 'LT', 'TM03',
    'W', 'LTI', 'SPI', 'C', 'API', 'MS24', 'NTP', 'ONG', 'SBI', 'KMB',
    'AB16', 'L', 'CRI', 'TM4', 'BF04'
]

results = []
for i in ids:
    url = f"https://priceapi.moneycontrol.com/pricefeed/nse/equitycash/{i}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        data = json.loads(res)
        if data.get('code') == '200':
            results.append(f"{i}: OK - {data['data'].get('pricecurrent')}")
        else:
            results.append(f"{i}: FAIL - {data.get('code')}")
    except Exception as e:
        results.append(f"{i}: ERR - {e}")

for r in results:
    print(r)
