from bs4 import BeautifulSoup
import lxml
import requests
from config import HEADERS, ITEM_URL, yag

response = requests.get(ITEM_URL, headers=HEADERS)
print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())

result = soup.select_one('.a-price-whole').getText()
title = soup.select_one('#productTitle').getText().strip()
price = float(result.split('.')[0])

target_price = 45

if price < target_price:
    yag.send(
        to="princeij56@gmail.com",
        subject=f"Buy Now !!!",
        contents=f"{title} \nis now ${price}. Buy it now! {ITEM_URL}"
    )
    
