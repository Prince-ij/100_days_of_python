import requests
from twilio.rest import Client

LAT = 10.457893
LONG = 7.453012
API_KEY = ""
API_ENDPOINT = "http://api.weatherapi.com/v1/current.json"
MY_NUM = +12707785487

params = {
    "key": API_KEY,
    "q": eval(f"{LAT}, {LONG}")
}


response = requests.get(API_ENDPOINT, params=params)
weather_condition = response.json()["current"]["condition"]["text"]
report = f"Hey Buddy, Today is gonna be a {weather_condition} day."

account_sid = 'AC3e54c7fa832bb21265e4c3827513ea34'
auth_token = ""
client = Client(account_sid, auth_token)


message = client.messages.create(
  from_= MY_NUM,
  to='+2347033662993',
  body=report
)
