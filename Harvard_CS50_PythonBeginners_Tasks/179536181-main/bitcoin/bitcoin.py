import requests
import sys
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    if len(sys.argv) == 1:
        raise Exception

    if len(sys.argv) == 2:
        n = float(sys.argv[1])
        try:
            response = requests.get(url, "rate_float")
            result = response.json()
            price = result["bpi"]["USD"]["rate_float"]
            total = price * n
            print("${:,.4f}".format(total))
        except requests.RequestException:
            print()
    else:
        sys.exit(1)

except Exception:
    sys.exit(1)
