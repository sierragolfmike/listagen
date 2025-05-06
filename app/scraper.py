import requests
from bs4 import BeautifulSoup
import re

def fetch_prices(item_name):
    query = item_name.replace(" ", "+")
    url = f"https://www.ebay.co.uk/sch/i.html?_nkw={query}&_sop=12"  # sorted by price + postage: lowest first

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data from eBay: HTTP {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    prices = []

    for item in soup.select('.s-item'):
        price_tag = item.select_one('.s-item__price')
        if price_tag:
            price_text = price_tag.get_text()
            match = re.search(r"£([\d,.]+)", price_text)
            if match:
                try:
                    price = float(match.group(1).replace(",", ""))
                    prices.append(price)
                except ValueError:
                    continue

    return prices
