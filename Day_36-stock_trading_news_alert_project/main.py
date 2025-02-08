from twilio.rest import Client
import datetime as dt
from datetime import timedelta
import requests

STOCK = "AAPL"
MY_NUM = +12707785487

ALPHAVANTAGE_API_KEY = ""
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = ""
NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"

yesterday = str(dt.datetime.today()-timedelta(days=1)).split()[0]
before_yesterday = str(dt.datetime.today()-timedelta(days=2)).split()[0]

alpha_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

news_param = {
    "from": before_yesterday,
    "category": "technology",
    "country": "us",
    "q": "Apple",
    "apikey": NEWS_API_KEY,
}


response = requests.get(ALPHAVANTAGE_ENDPOINT, alpha_param)
response.raise_for_status()


yesterday_price = response.json()['Time Series (Daily)'][yesterday]['4. close']
before_yesterday_price = response.json()['Time Series (Daily)'][before_yesterday]['4. close']

difference = (float(yesterday_price) - float(before_yesterday_price))
percent_change = round((difference / float(yesterday_price)) * 100)


if percent_change > 0:
    indicator = "🔺"
else:
    indicator = "🔻"
news = requests.get(NEWS_API_ENDPOINT, news_param)
news.raise_for_status()
articles = news.json()['articles'][:3]

report = f"TSLA: {indicator}{percent_change}%"
for i in range(3):
    headline = articles[i]['title']
    brief = articles[i]['description']
    report += f"\n\nHeadline: {headline}\nBrief: {brief}\n\n"


auth_token = ''
client = Client(account_sid, auth_token)


message = client.messages.create(
from_= MY_NUM,
to='+2347033662993',
body=report
)

print(message())
